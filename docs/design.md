# Fabric SDK Design Spec

Here we discuss the design principle and architecture consideration.

In total, we have several modules:

* Client: The top-level class. Users should mostly use this as the entry point.
* Chain: Represent one chain. Provide Blockchain related operations.
* MemberService: Membership related operations.

## Client
Main interaction handler with end user.

Client can maintain several chains.

### new_chain
Init a chain instance with given name.

**Params**

* name (str): The name of the chain

**Returns** (Chain instance): The inited chain instance.

### get_chain
Get a chain instance

**Params**

* name (str): The name of the chain

**Returns** (Chain instance or None): Get the chain instance with the name. 

### key_related_process
TODO.

store or change persistent and private date

**Params**

* name (str): The name of the key

**Returns** (): The result

### get_memberservices()
Get the MemberService for a chain

**Params**

* chain_id (str): The id of the chain

**Returns** (MemberService instance): The memberservice instance.

### member_register

Register a user.

**Params**

* name (str): The name of the user
* password (str): The password of the user

**Returns** 

* True or False (Bool): The registration result.

### member_enroll

Enroll a member.

**Params**

* name (str): The name of the chain
* password (str): The password of the user

**Returns** 
* certs (Cert data): The created data

### transaction_deploy

Deploy a chaincode to peer.

**Params**

* peer (Peer): The instance of the peer
* transaction (Transaction): The instance of the transaction

**Returns** 
* result(TransactionResponse): The return result response

### transaction_invoke
Invoke a chaincode to peer.

**Params**

* peer (Peer): The instance of the peer
* transaction (Transaction): The instance of the transaction

**Returns** 
* result(TransactionResponse): The return result response

### transaction_query
Query a chaincode from peer.

**Params**

* peer (Peer): The instance of the peer
* transaction (Transaction): The instance of the transaction

TODO: maybe use the transaction id is enough

**Returns** 
* result(TransactionResponse): The return result response


## Chain

A chain consists of several peers. Possible to have a membersrvc peer node.

### add_peer

Add peer to a chain

**Params**

* name (str): The name of the chain
* type (str): The type of the peer
* address (str): The address of the chain

**Returns** 
* result(Bool): The response

### get_peers

Get peers of a chain

**Params**

* None

**Returns** 

* (Peer list): The peer list on the  chain

### get_status

Get chain statue.

**Params**

* None

**Returns** 
* (Chain status): The status of the chain instance.

### transaction_deploy

Deploy a transaction.

**Params**

* transaction (Transaction): The transaction

**Returns** 

* (Chain instance): The inited chain instance.

### transaction_invoke

Invoke a transaction.

**Params**

* transaction (Transaction): The transaction

**Returns**

* result(TransactionResponse): The return result response
### transaction_query

Query the chain.

**Params**

* name (str): The name of the chain

TODO:
* other_params ():

**Returns** (TransactionResponse): The return result response

### get_membersrvc

Get a MemberService.

**Params**

* name (str): The name of the member service

**Returns** (MemberService instance): The member service instance.

### _transaction_send

Send a transaction to peer, this will support the transaction related methods.


## MemberService

### get_name

TODO:do we need this?

Get member name.

**Params**

* name (str): The name of the chain

**Returns** (str): The name of the MemberService instance.


### register_user

Implement register user.

**Params**

* name (str): The name of the user
* password (str): The password of the user

**Returns** (True or False): The result

### is_registered

Determine if this user has been registered.

**Params**

* name (str): The name of the user

**Returns** (True or False): The result

### enroll

Implement enroll

**Params**

* cert (Cert): The cert of the user

**Returns** (True or False): The result

### is_enrolled

Determine if this name has been enrolled

**Params**

* name (str): The name of the member

**Returns** (True or False): The result

### delete_enrollment

delete member

**Params**

* name (str): The name of the member

**Returns** (True or False): The result
### get_enrollment
Get member info

**Params**

* name (str): The name of the enrollment

**Returns** (Chain instance): The inited chain instance.

### get_enrollment_ecert
Get enrollment certificates for enroll

**Params**

* name (str): The name of the chain

**Returns** (Cert): The cert

### get_enrollment_tcert

Use for transaction, there is a 1-to-1 relationship between TCert and Transaction

**Params**

* name (str): The name of the chain

**Returns** (Tcert): The Tcert

### get_transaction
Get a transaction from member.

**Params**

* name (str): The name of the member

**Returns** (Transactions): The transactions.

### process_confidentiality
Process some security and identity info.

**Params**

* name (str): The name of the chain

**Returns** (Chain instance): The inited chain instance.


## Reference

[Node.js SDK](http://169.53.62.117/site/Setup/NodeSDK-setup/)
