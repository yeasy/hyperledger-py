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
import json
import logging

import six

from .. import errors

log = logging.getLogger(__name__)


def convert_to_hostname(url):
    return url.replace('http://', '').replace('https://', '').split('/', 1)[0]


def decode_auth(auth):
    if isinstance(auth, six.string_types):
        auth = auth.encode('ascii')
    s = base64.b64decode(auth)
    login, pwd = s.split(b':', 1)
    return login.decode('utf8'), pwd.decode('utf8')


def encode_header(auth):
    auth_json = json.dumps(auth).encode('ascii')
    return base64.urlsafe_b64encode(auth_json)


def parse_auth(entries, raise_on_error=False):
    """ Parses authentication entries

    :param entries:        Dict of authentication entries.
    :param raise_on_error: If set to true, an invalid format will raise
                      InvalidConfigFile

    :return: Authentication registry.
    """

    conf = {}
    for registry, entry in six.iteritems(entries):
        if not isinstance(entry, dict):
            log.debug(
                'Config entry for key {0} is not auth config'.format(registry)
            )
            # We sometimes fall back to parsing the whole config as if it was
            # the auth config by itself, for legacy purposes. In that case, we
            # fail silently and return an empty conf if any of the keys is not
            # formatted properly.
            if raise_on_error:
                raise errors.InvalidConfigFile(
                    'Invalid configuration for registry {0}'.format(registry)
                )
            return {}
        if 'auth' not in entry:
            # Starting with engine v1.11 (API 1.23), an empty dictionary is
            # a valid value in the auths config.
            log.debug(
                'Auth data for {0} is absent. Client might be using a '
                'credentials store instead.'
            )
            return {}

        username, password = decode_auth(entry['auth'])
        log.debug(
            'Found entry (registry={0}, username={1})'
            .format(repr(registry), repr(username))
        )
        conf[registry] = {
            'username': username,
            'password': password,
            'email': entry.get('email'),
            'serveraddress': registry,
        }
    return conf


def load_config(config_path=None):
    """ Loads authentication data from a Hyperledger configuration file

    TODO: implement this method
    Check the given root directory or if config_path is passed use given path.

    :param config_path: configuration file path
    :return: config dict
    """
    if config_path:
        return {}
    return {}
