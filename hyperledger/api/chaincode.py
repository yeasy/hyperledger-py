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
from ..constants import CHAINCODE_CONFIDENTIAL_PUB, CHAINCODE_LANG_GO, \
    DEFAULT_CHAINCODE_METHODS, DEFAULT_CHAINCODE_PATH, \
    DEFAULT_CHAINCODE_INIT_FUNC, DEFAULT_CHAINCODE_INIT_ARGS


class ChainCodeApiMixin(object):
    """ Mixin of the chaincode related APIs

    # noqa
    See https://github.com/hyperledger/fabric/blob/master/docs/API/CoreAPI.md#chaincode.
    """
    def _exec_action(self,
                     method,
                     type,
                     chaincodeID,
                     function,
                     args,
                     id,
                     secure_context=None,
                     confidentiality_level=CHAINCODE_CONFIDENTIAL_PUB,
                     metadata=None):
        """ Private method to implement the deploy, invoke and query actions

        Following http://www.jsonrpc.org/specification.

        :param method: Chaincode action to exec. MUST within
        DEFAULT_CHAINCODE_METHODS.
        :param type: chaincode language type: 1 for golang, 2 for node.
        :param chaincodeID: May include name or path.
        :param function: chaincode function name.
        :param args: chaincode function args.
        :param id: JSON-RPC requires this value for a response.
        :param secure_context: secure context if enable authentication.
        :param confidentiality_level: level of confidentiality.
        :param metadata: Metadata by client.

        """
        if method not in DEFAULT_CHAINCODE_METHODS:
            self.logger.error('Non-supported chaincode method: '+method)

        data = {
            "jsonrpc": "2.0",  # JSON-RPC protocol version. MUST be "2.0".
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

    def chaincode_deploy(self, chaincode_name=None,
                         chaincode_path=DEFAULT_CHAINCODE_PATH,
                         type=CHAINCODE_LANG_GO,
                         function=DEFAULT_CHAINCODE_INIT_FUNC,
                         args=DEFAULT_CHAINCODE_INIT_ARGS, id=1,
                         secure_context=None,
                         confidentiality_level=CHAINCODE_CONFIDENTIAL_PUB,
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

        :param chaincode_name: chaincode name is only required in dev mode
        :param chaincode_path: path of the chaincode in local or repo URL
        :param type:
        :param function:
        :param args:
        :param id:
        :param secure_context:
        :param confidentiality_level:
        :param metadata:
        :return: json obj of the chaincode instance
        """
        if not chaincode_name:
            chaincodeID={"path": chaincode_path}
        else:
            chaincodeID={
                "name": chaincode_name,
                "path": chaincode_path
            }
        return self._exec_action(method="deploy", type=type,
                                 chaincodeID=chaincodeID,
                                 function=function, args=args, id=id,
                                 secure_context=secure_context,
                                 confidentiality_level=confidentiality_level,
                                 metadata=metadata)

    def chaincode_invoke(self, chaincode_name, type=CHAINCODE_LANG_GO,
                         function=DEFAULT_CHAINCODE_INIT_FUNC,
                         args=DEFAULT_CHAINCODE_INIT_ARGS, id=1,
                         secure_context=None,
                         confidentiality_level=CHAINCODE_CONFIDENTIAL_PUB,
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
        return self._exec_action(method="invoke", type=type,
                                 chaincodeID={"name": chaincode_name},
                                 function=function, args=args, id=id,
                                 secure_context=secure_context,
                                 confidentiality_level=confidentiality_level,
                                 metadata=metadata)

    def chaincode_query(self, chaincode_name, type=CHAINCODE_LANG_GO,
                        function="query",
                        args=["a"], id=1,
                        secure_context=None,
                        confidentiality_level=CHAINCODE_CONFIDENTIAL_PUB,
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
        return self._exec_action(method="query", type=type,
                                 chaincodeID={"name": chaincode_name},
                                 function=function, args=args, id=id,
                                 secure_context=secure_context,
                                 confidentiality_level=confidentiality_level,
                                 metadata=metadata)
