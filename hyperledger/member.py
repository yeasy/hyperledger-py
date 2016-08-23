

#  A member is an entity to interact with the chain
#  Can be an end user, or a peer node
class Member(object):
    def __init__(self, chain):
        self.chain = chain
