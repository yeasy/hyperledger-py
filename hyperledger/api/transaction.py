#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


class TransactionApiMixin(object):
    def transaction_get(self, tran_uuid):
        """ GET /transactions/{UUID}

        Use the /transactions/{UUID} endpoint to retrieve an individual
        transaction matching the UUID from the blockchain. The returned
        transaction message is defined inside fabric.proto.

        ```golang
        message Transaction {
            enum Type {
                UNDEFINED = 0;
                CHAINCODE_DEPLOY = 1;
                CHAINCODE_INVOKE = 2;
                CHAINCODE_QUERY = 3;
                CHAINCODE_TERMINATE = 4;
            }
            Type type = 1;
            bytes chaincodeID = 2;
            bytes payload = 3;
            string uuid = 4;
            google.protobuf.Timestamp timestamp = 5;

            ConfidentialityLevel confidentialityLevel = 6;
            bytes nonce = 7;

            bytes cert = 8;
            bytes signature = 9;
        }
        ```

        :param tran_uuid: The uuid of the transaction to retrieve
        :return: json body of the transaction info
        """
        res = self._get(self._url("/transactions/{0}", tran_uuid))
        return self._result(res, True)
