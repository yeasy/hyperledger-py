#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from __future__ import print_function
from hyperledger.client import Client

import sys
import time

API_URL = 'http://127.0.0.1:5000'


def query_value(chaincode_name, arg_list):
    """
    Query a list of values.

    :param chaincode_name: The name of the chaincode.
    :param arg_list: List of arguments.
    :return: A list of values.
    """
    result = []
    for arg in arg_list:
        res = c.chaincode_query(chaincode_name=chaincode_name, function="query",
                                args=[arg])
        assert res['result']['status'] == 'OK'
        result.append(res['result']['message'])

    return result


# Usage:
# * python function_test.py [API_URL=http://127.0.0.1:5000] will deploy first
# * python function_test.py [API_URL=http://127.0.0.1:5000] [chaincode_name]
# E.g.,
# "f389486d91f54d1f8775940f24b1d3bd9f8a8e75d364e158ac92328ddacad629607a3c42be156fc4a7da7173adca2ac7d7eef29afc59c6f07f3ad14abee34f68"
if __name__ == '__main__':
    if len(sys.argv) not in [2, 3]:
        print("Usage: python function_test.py ["
              "API_URL=http://127.0.0.1:5000] [chaincode_name]")
        exit()
    API_URL = sys.argv[1]
    if len(sys.argv) == 3:
        chaincode_name = sys.argv[2]

    c = Client(base_url=API_URL)

    if not chaincode_name:
        print("Test: deploy a chaincode")
        res = c.chaincode_deploy()
        chaincode_name = res['result']['message']
        assert res['result']['status'] == 'OK'
        print("chaincode deployed with name " + chaincode_name)

    print("Check the initial value: a, b")
    print(query_value(chaincode_name, ["a", "b"]))

    print("Test: invoke a chaincode: a-->b 1")
    res = c.chaincode_invoke(chaincode_name=chaincode_name, function="invoke",
                             args=["a", "b", "1"])

    # TODO: sleep 1 second till invoke done.
    time.sleep(2)

    print("Check the after value: a, b")
    print(query_value(chaincode_name, ["a", "b"]))

    print("Test: list the peers")
    res = c.peer_list()
    print(res)
    assert len(res['peers']) > 0

    print("Test: list the chain")
    res = c.chain_list()
    print(res)
    assert res['height'] > 0

    print("Test: get the first block")
    print(c.block_get(block='1'))

