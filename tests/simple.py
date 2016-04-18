
from hyperledger.client import Client


if __name__ == '__main__':
    c = Client(base_url='http://9.186.100.88:5000')
    print c.block_get(block='1')
    print c.chain_list()
