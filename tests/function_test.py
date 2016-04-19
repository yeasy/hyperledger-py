
from __future__ import print_function
from hyperledger.client import Client

import sys


TEST_URL = 'http://9.186.100.88:5000'

def query_value(chaincode_id, arg_list):
    """
    Query a list of values.

    :param chaincode_id: The id of the chaincode.
    :param arg_list: List of arguments.
    :return: A list of values.
    """
    result = []
    for arg in arg_list:
        res = c.chaincode_query(chaincode_name=chaincode_id, function="query",
                                args=[arg])
        assert res['result']['status'] == 'OK'
        result.append(res['result']['message'])

    return result


# Given chaincode_id as the param will ignore the deployment
# E.g.,
# "f389486d91f54d1f8775940f24b1d3bd9f8a8e75d364e158ac92328ddacad629607a3c42be156fc4a7da7173adca2ac7d7eef29afc59c6f07f3ad14abee34f68"
if __name__ == '__main__':
    chaincode_id = ""
    c = Client(base_url=TEST_URL)
    if len(sys.argv) == 2:
        chaincode_id = sys.argv[1]

    if not chaincode_id:
        print("Test: deploy a chaincode")
        res = c.chaincode_deploy()
        chaincode_id = res['result']['message']
        assert res['result']['status'] == 'OK'
        print("chaincode deployed with name " + chaincode_id)

    query_value(chaincode_id, ["a","b"])

    print("Test: invoke a chaincode: a-->b 1")
    res = c.chaincode_invoke(chaincode_name=chaincode_id, function="invoke",
                             args=["a", "b", "1"])

    # TODO: here we may need to sleep a while till invoke done.

    query_value(chaincode_id, ["a","b"])

    print("Test: get a block")
    print(c.block_get(block='1'))

    print("Test: list a block")
    res = c.chain_list()
    print(res)
    assert res['height'] > 0
