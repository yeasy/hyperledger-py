#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


import logging
import requests
import requests.exceptions
import six

from . import api
from . import auth
from . import constants
from . import errors

from .utils import update_headers, kwargs_from_env


def from_env(**kwargs):
    return Client.from_env(**kwargs)


class Client(
        requests.Session,
        api.BlockApiMixin,
        api.BlockChainApiMixin,
        api.ChainCodeApiMixin,
        api.NetworkApiMixin,
        api.RegistrarApiMixin,
        api.TransactionApiMixin):
    def __init__(self, base_url=constants.DEFAULT_BASE_URL,
                 version=constants.DEFAULT_API_VERSION,
                 timeout=constants.DEFAULT_TIMEOUT_SECONDS, tls=False):
        super(Client, self).__init__()

        if tls and not base_url:
            raise errors.TLSParameterError(
                'If using TLS, the base_url argument must be provided.'
            )

        self.base_url = base_url
        self.timeout = timeout
        self._version = version
        self._auth_configs = auth.load_config()

        self.logger = logging.getLogger(__name__)

    def _set_request_timeout(self, kwargs):
        """Prepare the kwargs for an HTTP request by inserting the timeout
        parameter, if not already present."""
        kwargs.setdefault('timeout', self.timeout)
        return kwargs

    def _raise_for_status(self, response, explanation=None):
        """Raises stored :class:`APIError`, if one occurred."""
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                raise errors.NotFound(e, response, explanation=explanation)
            raise errors.APIError(e, response, explanation=explanation)

    def _result(self, response, json=False, binary=False):
        assert not (json and binary)
        self._raise_for_status(response)

        if json:
            return response.json()
        if binary:
            return response.content
        return response.text

    @update_headers
    def _post(self, url, **kwargs):
        return self.post(url, **self._set_request_timeout(kwargs))

    @update_headers
    def _get(self, url, **kwargs):
        return self.get(url, **self._set_request_timeout(kwargs))

    @update_headers
    def _put(self, url, **kwargs):
        return self.put(url, **self._set_request_timeout(kwargs))

    @update_headers
    def _delete(self, url, **kwargs):
        return self.delete(url, **self._set_request_timeout(kwargs))

    def _url(self, pathfmt, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, six.string_types):
                raise ValueError(
                    'Expected a string but found {0} ({1}) '
                    'instead'.format(arg, type(arg))
                )

        args = map(six.moves.urllib.parse.quote_plus, args)

        if kwargs.get('versioned_api', False):  # TODO: default to True later
            return '{0}/v{1}{2}'.format(
                self.base_url, self._version, pathfmt.format(*args)
            )
        else:
            return '{0}{1}'.format(self.base_url, pathfmt.format(*args))

    @classmethod
    def from_env(cls, **kwargs):
        return cls(**kwargs_from_env(**kwargs))
