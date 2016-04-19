
from hyperledger.client import Client

TEST_URL = 'http://9.186.100.88:5000'

if __name__ == '__main__':
    c = Client(base_url=TEST_URL)
    print "Test: deploy a chaincode"
    res = c.chaincode_deploy()
    chaincode_id = res['result']['message']
    print "chaincode deployed with name " + chaincode_id
    assert res['result']['status'] == 'OK'

    print "Test: get a block"
    print c.block_get(block='1')

    print "Test: list a block"
    res = c.chain_list()
    print res
    assert res['height'] > 0
