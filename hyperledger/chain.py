

#  A chain means a hyperledger fabric chain, of several fabric nodes.
class Chain(object):
    def __init__(self, name):
        self.peers = []
        self.security_enabled = True
        self.members = {}
        self.tcert_batch_size = 200
        self.dev_mode = False
        self.dev_mode = False
        self.pre_fetch_mode = True
        self.deploy_wait_time = 20
        self.invoke_wait_time = 5
        self.name = name
