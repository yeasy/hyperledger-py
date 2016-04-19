#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


import json
from ..constants import DEFAULT_CHAINCODE_METHODS, DEFAULT_CHAINCODE_PATH, DEFAULT_CHAINCODE_INIT_FUNC, DEFAULT_CHAINCODE_INIT_ARGS, DEFAULT_TIMEOUT_SECONDS

class ChainCodeApiMixin(object):
    """
    See https://github.com/hyperledger/fabric/blob/master/docs/API/CoreAPI.md#chaincode.
    """
    def _chaincode_exec(self,
                        jrpc_ver="2.0",
                        method="query",
                        type=1,
                        chaincodeID={},
                        function=DEFAULT_CHAINCODE_INIT_FUNC,
                        args=DEFAULT_CHAINCODE_INIT_ARGS,
                        id=1,
                        timeout=DEFAULT_TIMEOUT_SECONDS,
                        secure_context=None,
                        confidentiality_level=0,
                        metadata=None):
        """
        Private method to implement the deploy, invoke and query actions.
        Following http://www.jsonrpc.org/specification.

        :param jrpc_ver: The JSON-RPC protocol version. MUST be exactly "2.0".
        :param method: Chaincode action to exec. MUST within
        DEFAULT_CHAINCODE_METHODS.
        :param type: chaincode language type: 1 for golang, 2 for node.
        :param chaincodeID: May include name or path.
        :param function: chaincode function name.
        :param args: chaincode function args.
        :param id: JSON-RPC requires this value for a response.
        :param timeout: timeout value.
        :param secure_context: secure context if enable authentication.
        :param confidentiality_level: level of confidentiality.
        :param metadata: Metadata by client.

        """
        if method not in DEFAULT_CHAINCODE_METHODS:
            self.logger.error('Non-supported chaincode method: '+method)

        data = {
            "jsonrpc": jrpc_ver,
            "method": method,
            "params": {
                "type": type,
                "chaincodeID": chaincodeID,
                "ctorMsg": {
                    "function": function,
                    "args": args
                }
            },
            "id": id
        }
        if not secure_context:
            data["params"]["secureContext"] = secure_context
        u = self._url("/chaincode")
        response = self._post(u, data=json.dumps(data))
        return self._result(response, True)

    def chaincode_deploy(self, chaincode_path=DEFAULT_CHAINCODE_PATH, type=1,
                         function=DEFAULT_CHAINCODE_INIT_FUNC,
                         args=DEFAULT_CHAINCODE_INIT_ARGS, id=1,
                         timeout=DEFAULT_TIMEOUT_SECONDS,
                         secure_context=None, confidentiality_level=0,
                         metadata=None):
        """
        POST host:port/chaincode

        {
          "jsonrpc": "2.0",
          "method": "deploy",
          "params": {
            "type": 1,
            "chaincodeID":{
                "path":"github.com/hyperledger/fabric/examples/chaincode/go/chaincode_example02"
            },
            "ctorMsg": {
            "function":"init",
            "args":["a", "1000", "b", "2000"]
            }
          },
          "id": 1
        }

        :return: json obj of the chaincode instance
        """
        return self._chaincode_exec(method="deploy", type=type,
                                    chaincodeID={"path": chaincode_path},
                                    function=function, args=args, id=id,
                                    timeout=timeout,
                                    secure_context=secure_context,
                                    confidentiality_level=confidentiality_level,
                                    metadata=metadata)

    def chaincode_invoke(self, chaincode_name, type=1,
                         function=DEFAULT_CHAINCODE_INIT_FUNC,
                         args=DEFAULT_CHAINCODE_INIT_ARGS, id=1,
                         timeout=DEFAULT_TIMEOUT_SECONDS,
                         secure_context=None, confidentiality_level=0,
                         metadata=None):
        """
        {
          "jsonrpc": "2.0",
          "method": "invoke",
          "params": {
              "type": 1,
              "chaincodeID":{
                  "name":"52b0d803fc395b5e34d8d4a7cd69fb6aa00099b8fabed83504ac1c5d61a425aca5b3ad3bf96643ea4fdaac132c417c37b00f88fa800de7ece387d008a76d3586"
              },
              "ctorMsg": {
                 "function":"invoke",
                 "args":["a", "b", "100"]
              }
          },
          "id": 3
        }
        :return: json obj of the chaincode instance
        """
        return self._chaincode_exec(method="invoke", type=type,
                                    chaincodeID={"name": chaincode_name},
                                    function=function, args=args, id=id,
                                    timeout=timeout,
                                    secure_context=secure_context,
                                    confidentiality_level=confidentiality_level,
                                    metadata=metadata)

    def chaincode_query(self, chaincode_name, type=1,
                        function="query",
                        args=["a"], id=1,
                        timeout=DEFAULT_TIMEOUT_SECONDS,
                        secure_context=None, confidentiality_level=0,
                        metadata=None):
        """
        {
          "jsonrpc": "2.0",
          "method": "query",
          "params": {
              "type": 1,
              "chaincodeID":{
                  "name":"52b0d803fc395b5e34d8d4a7cd69fb6aa00099b8fabed83504ac1c5d61a425aca5b3ad3bf96643ea4fdaac132c417c37b00f88fa800de7ece387d008a76d3586"
              },
              "ctorMsg": {
                 "function":"query",
                 "args":["a"]
              }
          },
          "id": 3
        }
        :return: json obj of the chaincode instance
        """
        return self._chaincode_exec(method="query", type=type,
                                    chaincodeID={"name": chaincode_name},
                                    function=function, args=args, id=id,
                                    timeout=timeout,
                                    secure_context=secure_context,
                                    confidentiality_level=confidentiality_level,
                                    metadata=metadata)
