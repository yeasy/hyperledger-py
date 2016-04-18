
from hyperledger.client import Client


if __name__ == '__main__':
    c = Client(base_url='http://9.186.100.88:5000')
    print "Test: deploy a chaincode"
    res = c.chaincode_deploy()
    chaincode_id = res['result']['message']
    print "chaincode deployed with name " + chaincode_id
    assert res['result']['status'] == 'OK'

    print "Test: get a block"
    print c.block_get(block='1')

    print "Test: list a block"
    print c.chain_list()
