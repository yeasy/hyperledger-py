# Copyright 2013 dotCloud inc.

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import base64
import os
import os.path
import json
import shlex
from distutils.version import StrictVersion
from fnmatch import fnmatch
from datetime import datetime

import six

from .. import errors
from .. import tls


DEFAULT_HTTP_HOST = "127.0.0.1"
DEFAULT_HTTP_PORT = "5000"
BYTE_UNITS = {
    'b': 1,
    'k': 1024,
    'm': 1024 * 1024,
    'g': 1024 * 1024 * 1024
}


def decode_json_header(header):
    data = base64.b64decode(header)
    if six.PY3:
        data = data.decode('utf-8')
    return json.loads(data)


def match_path(path, pattern):
    pattern = pattern.rstrip('/')
    pattern_components = pattern.split('/')
    path_components = path.split('/')[:len(pattern_components)]
    return fnmatch('/'.join(path_components), pattern)


def compare_version(v1, v2):
    """TODO: Compare hyperledger versions

    >>> v1 = '1.1'
    >>> v2 = '1.10'
    >>> compare_version(v1, v2)
    1
    >>> compare_version(v2, v1)
    -1
    >>> compare_version(v2, v2)
    0
    """
    s1 = StrictVersion(v1)
    s2 = StrictVersion(v2)
    if s1 == s2:
        return 0
    elif s1 > s2:
        return -1
    else:
        return 1


def version_lt(v1, v2):
    return compare_version(v1, v2) > 0


def version_gte(v1, v2):
    return not version_lt(v1, v2)


def convert_tmpfs_mounts(tmpfs):
    if isinstance(tmpfs, dict):
        return tmpfs

    if not isinstance(tmpfs, list):
        raise ValueError(
            'Expected tmpfs value to be either a list or a dict, found: {}'
            .format(type(tmpfs).__name__)
        )

    result = {}
    for mount in tmpfs:
        if isinstance(mount, six.string_types):
            if ":" in mount:
                name, options = mount.split(":", 1)
            else:
                name = mount
                options = ""

        else:
            raise ValueError(
                "Expected item in tmpfs list to be a string, found: {}"
                .format(type(mount).__name__)
            )

        result[name] = options
    return result


def parse_repository_tag(repo_name):
    parts = repo_name.rsplit('@', 1)
    if len(parts) == 2:
        return tuple(parts)
    parts = repo_name.rsplit(':', 1)
    if len(parts) == 2 and '/' not in parts[1]:
        return tuple(parts)
    return repo_name, None


def datetime_to_timestamp(dt):
    """Convert a UTC datetime to a Unix timestamp"""
    delta = dt - datetime.utcfromtimestamp(0)
    return delta.seconds + delta.days * 24 * 3600


def longint(n):
    if six.PY3:
        return int(n)
    else:
        return long(n)  # noqa


def parse_bytes(s):
    if isinstance(s, six.integer_types + (float,)):
        return s
    if len(s) == 0:
        return 0

    if s[-2:-1].isalpha() and s[-1].isalpha():
        if s[-1] == "b" or s[-1] == "B":
            s = s[:-1]
    units = BYTE_UNITS
    suffix = s[-1].lower()

    # Check if the variable is a string representation of an int
    # without a units part. Assuming that the units are bytes.
    if suffix.isdigit():
        digits_part = s
        suffix = 'b'
    else:
        digits_part = s[:-1]

    if suffix in units.keys() or suffix.isdigit():
        try:
            digits = longint(digits_part)
        except ValueError:
            raise errors.HyperledgerException(
                'Failed converting the string value for memory ({0}) to'
                ' an integer.'.format(digits_part)
            )

        # Reconvert to long for the final result
        s = longint(digits * units[suffix])
    else:
        raise errors.HyperledgerException(
            'The specified value for memory ({0}) should specify the'
            ' units. The postfix should be one of the `b` `k` `m` `g`'
            ' characters'.format(s)
        )

    return s


def host_config_type_error(param, param_value, expected):
    error_msg = 'Invalid type for {0} param: expected {1} but found {2}'
    return TypeError(error_msg.format(param, expected, type(param_value)))


def host_config_version_error(param, version, less_than=True):
    operator = '<' if less_than else '>'
    error_msg = '{0} param is not supported in API versions {1} {2}'
    return errors.InvalidVersion(error_msg.format(param, operator, version))


def host_config_value_error(param, param_value):
    error_msg = 'Invalid value for {0} param: {1}'
    return ValueError(error_msg.format(param, param_value))


def normalize_links(links):
    if isinstance(links, dict):
        links = six.iteritems(links)

    return ['{0}:{1}'.format(k, v) for k, v in sorted(links)]


def split_command(command):
    if six.PY2 and not isinstance(command, six.binary_type):
        command = command.encode('utf-8')
    return shlex.split(command)


def format_environment(environment):
    def format_env(key, value):
        if value is None:
            return key
        return '{key}={value}'.format(key=key, value=value)
    return [format_env(*var) for var in six.iteritems(environment)]


def kwargs_from_env(ssl_version=None, assert_hostname=None, environment=None):
    if not environment:
        environment = os.environ
    host = environment.get('HYPERLEDGER_HOST')

    # empty string for cert path is the same as unset.
    cert_path = environment.get('HYPERLEDGER_CERT_PATH') or None

    # empty string for tls verify counts as "false".
    # Any value or 'unset' counts as true.
    tls_verify = environment.get('HYPERLEDGER_TLS_VERIFY')
    if tls_verify == '':
        tls_verify = False
    else:
        tls_verify = tls_verify is not None
    enable_tls = cert_path or tls_verify

    params = {}

    if host:
        params['base_url'] = (
            host.replace('tcp://', 'https://') if enable_tls else host
        )

    if not enable_tls:
        return params

    if not cert_path:
        cert_path = os.path.join(os.path.expanduser('~'), '.hyperledger')

    if not tls_verify and assert_hostname is None:
        # assert_hostname is a subset of TLS verification,
        # so if it's not set already then set it to false.
        assert_hostname = False

    params['tls'] = tls.TLSConfig(
        client_cert=(os.path.join(cert_path, 'cert.pem'),
                     os.path.join(cert_path, 'key.pem')),
        ca_cert=os.path.join(cert_path, 'ca.pem'),
        verify=tls_verify,
        ssl_version=ssl_version,
        assert_hostname=assert_hostname,
    )

    return params
