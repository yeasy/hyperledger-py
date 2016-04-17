import functools

from .. import errors
from . import utils


def minimum_version(version):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            if utils.version_lt(self._version, version):
                raise errors.InvalidVersion(
                    '{0} is not available for version < {1}'.format(
                        f.__name__, version
                    )
                )
            return f(self, *args, **kwargs)
        return wrapper
    return decorator


def update_headers(f):
    def inner(self, *args, **kwargs):
        if 'HttpHeaders' in self._auth_configs:
            if 'headers' not in kwargs:
                kwargs['headers'] = self._auth_configs['HttpHeaders']
            else:
                kwargs['headers'].update(self._auth_configs['HttpHeaders'])
        return f(self, *args, **kwargs)
    return inner
