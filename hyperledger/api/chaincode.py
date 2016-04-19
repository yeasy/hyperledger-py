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
from ..constants import DEFAULT_CHAINCODE_PATH, DEFAULT_CHAINCODE_FUNC, \
    DEFAULT_CHAINCODE_ARGS, DEFAULT_TIMEOUT_SECONDS

class ChainCodeApiMixin(object):
    def _chaincode_action(self, jsonrpc="2.0", method="query", type=1,
                          chaincodeID={},
                          function=DEFAULT_CHAINCODE_FUNC,
                          args=DEFAULT_CHAINCODE_ARGS,
                          id=1, timeout=DEFAULT_TIMEOUT_SECONDS,
                          secureContext=None, ConfidentialityLevel=0,
                          metadata=None):
        data = {
            "jsonrpc": jsonrpc,
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
        u = self._url("/chaincode")
        response = self._post(u, data=json.dumps(data))
        return self._result(response, True)

    def chaincode_deploy(self):
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
        return self._chaincode_action(method="deploy",
                                      chaincodeID={"path": DEFAULT_CHAINCODE_PATH})

    def chaincode_invoke(self, chaincode_name):
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
        return self._chaincode_action(method="invoke",
                                      chaincodeID={"name": chaincode_name})
