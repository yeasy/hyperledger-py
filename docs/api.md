# Client API
Here we will show the usage of each client API.

First you need to import the hyperledger client and create one instance.

```python
>>> from hyperledger.client import Client
>>> c = Client(base_url="http://127.0.0.1:7050")
```

**Params**:

* base_url (str): Refers to the protocol+hostname+port where the Hyperledger
 service listening on.
* version (str): The version of the API the client will use. 
* timeout (int): The HTTP request timeout, in seconds. Default to 
`DEFAULT_TIMEOUT_SECONDS`.
* tls (bool): Whether to use tls. Default to `False`.

****

## Block APIs

### block_get
The `block_get()` function will get a specific block and return as a json object.

**Params**

* block (str): The block to retrieve.

**Returns** (dict of [Block](https://github.com/hyperledger/fabric/blob/master/protos/fabric.proto)): The info of that block.

```python
>>> from hyperledger.client import Client
>>> c = Client(base_url="http://127.0.0.1:7050")
>>> c.block_get("1")
{u'stateHash': u'EY61Ad/+c6fl+tVnxw5JQFWgJMZQswBaX+cytJyuMa/fwvuffTohLt6ShoiJWb245IiRiTTZ/50WN/uViZSnoA==', u'previousBlockHash': u'RrndKwuojRMjOz/rdD7rJD/NUupiuBuCtQwnZG7Vdi/XXcTd2MDyAMsFAZ1ntZL2/IIcSUeatIZAKS6ss7fEvg==', u'nonHashData': {u'localLedgerCommitTimestamp': {u'seconds': 1460709218, u'nanos': 581261246}}, u'transactions': [{u'chaincodeID': u'CkdnaXRodWIuY29tL2h5cGVybGVkZ2VyL2ZhYnJpYy9leGFtcGxlcy9jaGFpbmNvZGUvZ28vY2hhaW5jb2RlX2V4YW1wbGUwMhKAATU4NDRiYzE0MmRjYzllNzg4Nzg1ZTAyNmUyMmM4NTU5NTdiMmM3NTRjOTEyNzAyYzU4ZDk5N2RlZGJjOWEwNDJmMDVkMTUyZjZkYjBmYmQ3ODEwZDk1YzFiODgwYzIxMDU2NmM5ZGUzMDkzYWFlMGFiNzZhZDJkOTBlOWNmYWE1', u'type': 1, u'payload': u'CukBCAESzAEKR2dpdGh1Yi5jb20vaHlwZXJsZWRnZXIvZmFicmljL2V4YW1wbGVzL2NoYWluY29kZS9nby9jaGFpbmNvZGVfZXhhbXBsZTAyEoABNTg0NGJjMTQyZGNjOWU3ODg3ODVlMDI2ZTIyYzg1NTk1N2IyYzc1NGM5MTI3MDJjNThkOTk3ZGVkYmM5YTA0MmYwNWQxNTJmNmRiMGZiZDc4MTBkOTVjMWI4ODBjMjEwNTY2YzlkZTMwOTNhYWUwYWI3NmFkMmQ5MGU5Y2ZhYTUaFgoEaW5pdBIBYRIDMTAwEgFiEgMyMDA=', u'timestamp': {u'seconds': 1460709198, u'nanos': 458532061}, u'uuid': u'5844bc142dcc9e788785e026e22c855957b2c754c912702c58d997dedbc9a042f05d152f6db0fbd7810d95c1b880c210566c9de3093aae0ab76ad2d90e9cfaa5'}]}
```

## Blockchain APIs
### chain_list
The `chain_list()` function will retrieve the current state of the blockchain.

**Returns** (dict of [BlockchainInfo](https://github.com/hyperledger/fabric/blob/master/protos/fabric.proto)): The info of that
 chain.

```python
>>> from hyperledger.client import Client
>>> c = Client(base_url="http://127.0.0.1:7050")
>>> c.chain_list()
{u'currentBlockHash': u'G1BHzva7RHbY/EMsT8swvRJmvO2RG4jVhiY8gw+sL/WGFl5x+qOk2gKLusxHcAFsEBOLV1kXfNfjJhpFHAwSPw==', u'previousBlockHash': u'ZJcfc/RCr+lYcQvtD4VvoUM4FGWHMPd9WSi7qekwdAedwJBs/Vpd4yoYl/FeerAdEJ7OXJokO1A7YBKNuC5h1A==', u'height': 29}
```

## Chaincode APIs

### chaincode_deploy
The `chaincode_deploy()` function will deploy a chaincode to the service.

**Params**
* chaincode_path (str): path to the chaincode. Default to 
`DEFAULT_CHAINCODE_PATH`.
* type (int): chaincode language type: `1` for golang, `2` for node. Default
 to `CHAINCODE_LANG_GO`.
* function (str): chaincode function name. Default to 
`DEFAULT_CHAINCODE_INIT_FUNC`
* args (str): chaincode function args. Default to 
`DEFAULT_CHAINCODE_INIT_ARGS`.
* id (int): JSON-RPC requires this value for a response. Default to `1`.
* secure_context (str): secure context if enable authentication. Default to 
`None`.
* confidentiality_level (int): level of confidentiality. Default to 
`CHAINCODE_CONFIDENTIAL_PUB`.
* metadata (str): Metadata by client.

**Returns** (dict of deployed [Chaincode](https://github.com/hyperledger/fabric/blob/master/protos/fabric.proto)): The info of that
 deployed result.

```python
>>> from hyperledger.client import Client
>>> c = Client(base_url="http://127.0.0.1:7050")
>>> c.chaincode_deploy()
{u'jsonrpc': u'2.0', u'result': {u'status': u'OK', u'message': u'f389486d91f54d1f8775940f24b1d3bd9f8a8e75d364e158ac92328ddacad629607a3c42be156fc4a7da7173adca2ac7d7eef29afc59c6f07f3ad14abee34f68'}, u'id': 1}
```

### chaincode_invoke
The `chaincode_invoke()` function will invoke a specific chaincode.

**Params**
* chaincode_name (str): Name of the chaincode. Usually returned by the 
deploy API.
* type (int): chaincode language type: `1` for golang, `2` for node. Default
 to `CHAINCODE_LANG_GO`.
* function (str): chaincode function name. Default to 
`DEFAULT_CHAINCODE_INIT_FUNC`
* args (str): chaincode function args. Default to 
`DEFAULT_CHAINCODE_INIT_ARGS`.
* id (int): JSON-RPC requires this value for a response. Default to `1`.
* secure_context (str): secure context if enable authentication. Default to 
`None`.
* confidentiality_level (int): level of confidentiality. Default to 
`CHAINCODE_CONFIDENTIAL_PUB`.
* metadata (str): Metadata by client.

**Returns** (dict of invoke result): The info of that invoke result.
 
```python
>>> from hyperledger.client import Client
>>> c = Client(base_url="http://127.0.0.1:7050")
>>> c.chaincode_invoke(chaincode_name="f389486d91f54d1f8775940f24b1d3bd9f8a8e75d364e158ac92328ddacad629607a3c42be156fc4a7da7173adca2ac7d7eef29afc59c6f07f3ad14abee34f68")
{u'jsonrpc': u'2.0', u'result': {u'status': u'OK', u'message': u'dd29ff47-b0c8-44a0-a1b1-d050e5c7bc82'}, u'id': 1}
```

### chaincode_query
The `chaincode_query()` function will query a specific chaincode.

**Params**
* chaincode_name (str): Name of the chaincode. Usually returned by the 
deploy API.
* type (int): chaincode language type: `1` for golang, `2` for node. Default
 to `CHAINCODE_LANG_GO`.
* function (str): chaincode function name. Default to 
`DEFAULT_CHAINCODE_INIT_FUNC`
* args (str): chaincode function args. Default to 
`DEFAULT_CHAINCODE_INIT_ARGS`.
* id (int): JSON-RPC requires this value for a response. Default to `1`.
* secure_context (str): secure context if enable authentication. Default to 
`None`.
* confidentiality_level (int): level of confidentiality. Default to 
`CHAINCODE_CONFIDENTIAL_PUB`.
* metadata (str): Metadata by client.

**Returns** (dict of [Chaincode](https://github.com/hyperledger/fabric/blob/master/protos/fabric.proto)): The info of that query result.
 
```python
>>> from hyperledger.client import Client
>>> c = Client(base_url="http://127.0.0.1:7050")
>>> c.chaincode_query(chaincode_name="f389486d91f54d1f8775940f24b1d3bd9f8a8e75d364e158ac92328ddacad629607a3c42be156fc4a7da7173adca2ac7d7eef29afc59c6f07f3ad14abee34f68", function="query", args=["a"])
{u'jsonrpc': u'2.0', u'result': {u'status': u'OK', u'message': u'9980'}, u'id': 1}
```

## Network APIs
### peer_list
The `peer_list()` function will retrieve information about the network of peer nodes comprising the blockchain network.

**Returns** (dict of [PeerEndpoint](https://github.com/hyperledger/fabric/blob/master/protos/fabric.proto)): The info of the peer nodes.

```python
>>> from hyperledger.client import Client
>>> c = Client(base_url="http://127.0.0.1:7050")
>>> c.peer_list()
{u'peers': [{u'type': 1, u'ID': {u'name': u'vp1'}, u'address': u'172.17.0.2:30303'}, {u'type': 1, u'ID': {u'name': u'vp2'}, u'address': u'172.17.0.3:30303'}]}
```
