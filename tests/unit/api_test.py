#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# flake8: noqa

import six
import sys
# import unittest

from .. import base
from hyperledger.client import Client

try:
    from unittest import mock
except ImportError:
    import mock


def fake_block_get():
    return {
        u'stateHash': u'EY61Ad/+c6fl+tVnxw5JQFWgJMZQswBaX+cytJyuMa/fwvuffTohLt6ShoiJWb245IiRiTTZ/50WN/uViZSnoA==',
        u'previousBlockHash': u'RrndKwuojRMjOz/rdD7rJD/NUupiuBuCtQwnZG7Vdi/XXcTd2MDyAMsFAZ1ntZL2/IIcSUeatIZAKS6ss7fEvg==',
        u'nonHashData': {
            u'localLedgerCommitTimestamp': {
                u'seconds': 1460709218,
                u'nanos': 581261246
            }
        },
        u'transactions': [
            {
                u'chaincodeID': u'CkdnaXRodWIuY29tL2h5cGVybGVkZ2VyL2ZhYnJpYy9leGFtcGxlcy9jaGFpbmNvZGUvZ28vY2hhaW5jb2RlX2V4YW1wbGUwMhKAATU4NDRiYzE0MmRjYzllNzg4Nzg1ZTAyNmUyMmM4NTU5NTdiMmM3NTRjOTEyNzAyYzU4ZDk5N2RlZGJjOWEwNDJmMDVkMTUyZjZkYjBmYmQ3ODEwZDk1YzFiODgwYzIxMDU2NmM5ZGUzMDkzYWFlMGFiNzZhZDJkOTBlOWNmYWE1',
                u'type': 1,
                u'payload': u'CukBCAESzAEKR2dpdGh1Yi5jb20vaHlwZXJsZWRnZXIvZmFicmljL2V4YW1wbGVzL2NoYWluY29kZS9nby9jaGFpbmNvZGVfZXhhbXBsZTAyEoABNTg0NGJjMTQyZGNjOWU3ODg3ODVlMDI2ZTIyYzg1NTk1N2IyYzc1NGM5MTI3MDJjNThkOTk3ZGVkYmM5YTA0MmYwNWQxNTJmNmRiMGZiZDc4MTBkOTVjMWI4ODBjMjEwNTY2YzlkZTMwOTNhYWUwYWI3NmFkMmQ5MGU5Y2ZhYTUaFgoEaW5pdBIBYRIDMTAwEgFiEgMyMDA=',
                u'timestamp': {
                    u'seconds': 1460709198,
                    u'nanos': 458532061
                },
                u'uuid': u'5844bc142dcc9e788785e026e22c855957b2c754c912702c58d997dedbc9a042f05d152f6db0fbd7810d95c1b880c210566c9de3093aae0ab76ad2d90e9cfaa5'
            }
        ]
    }


def fake_chain_list():
    return {
        u'currentBlockHash': u'JedZ+FaHokNOtUFQYWt3BHxPRFwh6FavHWICLosWYzA96AdoKhC8aMSACA4kRIfOdwA8YT9UkN3rzkAfdq/LdQ==',
        u'previousBlockHash': u'BbRQp7FNSBpLxqdcXNp6+2ZPx3Q5j8vbtrHxIzsf45QJMAXHv6dW1foB0LAv+/UOuu6L5okn3/iLvRNmEFMO9g==',
        u'height': 4
    }


def fake_chaincode_deploy():
    return {
        u'jsonrpc': u'2.0',
        u'result': {
            u'status': u'OK',
            u'message': u'4c87036dd42ad239c83bf30d4a1da0aeb0dfa88b7b584c68c327c7a6001f3067dfdd60e7f695a27e45a952da43eb8d3a0120707c739a8fa0cf90e91a51ad662f'
        },
        u'id': 1
    }


def fake_chaincode_invoke(chaincode_name):
    return {
        u'jsonrpc': u'2.0',
        u'result': {
            u'status': u'OK',
            u'message': u'3123a1a4-9901-47d8-b3fb-e2fcae605605'
        },
        u'id': 1
    }


def fake_chaincode_query(chaincode_name):
    return {
        u'jsonrpc': u'2.0',
        u'result': {
            u'status': u'OK',
            u'message': u'20015'
        },
        u'id': 1
    }


class HyperledgerClientTest(base.Cleanup, base.BaseTestCase):
    def setUp(self):
        self.c = Client(base_url="http://127.0.0.1:5000")
        pass

    def tearDown(self):
        pass

    def assertIn(self, object, collection):
        if six.PY2 and sys.version_info[1] <= 6:
            return self.assertTrue(object in collection)
        return super(HyperledgerClientTest, self).assertIn(object, collection)


class HyperledgerApiTest(HyperledgerClientTest):
    def test_block_get(self):
        pass
