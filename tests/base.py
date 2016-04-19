#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import sys
import unittest

import pytest
import six

import hyperledger


class BaseTestCase(unittest.TestCase):
    def assertIn(self, object, collection):
        if six.PY2 and sys.version_info[1] <= 6:
            return self.assertTrue(object in collection)
        return super(BaseTestCase, self).assertIn(object, collection)


def requires_api_version(version):
    return pytest.mark.skipif(
        hyperledger.utils.version_lt(
            hyperledger.constants.DEFAULT_HYPERLEDGER_API_VERSION, version
        ),
        reason="API version is too low (< {0})".format(version)
    )


class Cleanup(object):
    if sys.version_info < (2, 7):
        # Provide a basic implementation of addCleanup for Python < 2.7
        def __init__(self, *args, **kwargs):
            super(Cleanup, self).__init__(*args, **kwargs)
            self._cleanups = []

        def tearDown(self):
            super(Cleanup, self).tearDown()
            ok = True
            while self._cleanups:
                fn, args, kwargs = self._cleanups.pop(-1)
                try:
                    fn(*args, **kwargs)
                except KeyboardInterrupt:
                    raise
                except:
                    ok = False
            if not ok:
                raise

        def addCleanup(self, function, *args, **kwargs):
            self._cleanups.append((function, args, kwargs))
