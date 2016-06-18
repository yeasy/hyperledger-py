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

# import base64
import json
import sys
import time
import timeit
#from timeit import Timer

API_URL = 'http://127.0.0.1:5000'

DEPLOY_WAIT=15


def query(chaincode_name, arg_list, validate=False):
    """
    Query a list of values.

    :param chaincode_name: The name of the chaincode.
    :param arg_list: List of arguments.
    :return: A list of values.
    """
    result, resp = [], {}
    for arg in arg_list:
        resp = c.chaincode_query(chaincode_name=chaincode_name,
                                 function="query",
                                 args=[arg])
        if not validate:
            continue
        if resp['result']['status'] == 'OK':
            result.append(resp['result']['message'])
            continue
        else:
            print("Error when querying")
        #try:
        #except KeyError as e:
        #    print("Exception")
        #    print(e)
        #    return None

    if validate:
        return result


# Usage:
# * python function_test.py [API_URL=http://127.0.0.1:5000] will deploy first
# * python function_test.py [API_URL=http://127.0.0.1:5000] [chaincode_name]
# E.g.,
# "f389486d91f54d1f8775940f24b1d3bd9f8a8e75d364e158ac92328ddacad629607a3c42be156fc4a7da7173adca2ac7d7eef29afc59c6f07f3ad14abee34f68"
if __name__ == '__main__':
    if len(sys.argv) not in [1, 2, 3]:
        print("Usage: python function_test.py ["
              "API_URL=http://127.0.0.1:5000] [chaincode_name]")
        exit()

    if len(sys.argv) >= 2:
        API_URL = sys.argv[1]
    chaincode_name = ""
    if len(sys.argv) >= 3:
        chaincode_name = sys.argv[2]

    c = Client(base_url=API_URL)

    print("Checking cluster at {}".format(API_URL))

    if not chaincode_name:
        print(">>>Test: deploy the default chaincode")
        res = c.chaincode_deploy(args=["a", "10000", "b", "20000"])
        chaincode_name = res['result']['message']
        assert res['result']['status'] == 'OK'
        print("Successfully deploy chaincode with returned name = " +
              chaincode_name)
        print("Wait {}s to make sure deployment is done.".format(DEPLOY_WAIT))
        time.sleep(DEPLOY_WAIT)


    print(">>>Check the initial value: a, b")
    values = query(chaincode_name, ["a", "b"], validate=True)
    print(values)
    #assert values == ['10000', '20000']

    duration=timeit.timeit("query(chaincode_name, ['a', 'b'])",
                           number=2000,
                           setup="from __main__ import query, chaincode_name")
    print("Query 2000 times, and calculate the time={}".format(duration))

    print(">>>Check the value again: a, b")
    values = query(chaincode_name, ["a", "b"], validate=True)
    print(values)

    exit(0)

    print(">>>Test: invoke a chaincode: a-->b 1")
    res = c.chaincode_invoke(chaincode_name=chaincode_name, function="invoke",
                             args=["a", "b", "1"])
    assert res["result"]["status"] == "OK"
    transaction_uuid = res["result"]["message"]
    print("Transaction id = {0}".format(transaction_uuid))

    # TODO: sleep 3 seconds till invoke done.
    print("Wait 5 seconds to make sure invoke is done.")
    time.sleep(5)

    print(">>>Check the after value: a, b")
    values = query(chaincode_name, ["a", "b"])
    print(values)
    assert values == ['9999', '20001']
    time.sleep(1)
