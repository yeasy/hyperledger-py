
from hyperledger.client import Client


if __name__ == '__main__':
    c = Client(base_url='http://9.186.100.88:5000')
    print c.block_list(block='1')
