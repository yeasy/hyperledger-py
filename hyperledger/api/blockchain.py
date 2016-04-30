#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


class BlockChainApiMixin(object):

    def chain_list(self):
        """ GET /chain

        Use the Chain API to retrieve the current state of the blockchain.
        The returned BlockchainInfo message is defined inside fabric.proto.

        message BlockchainInfo {
            uint64 height = 1;
            bytes currentBlockHash = 2;
            bytes previousBlockHash = 3;
        }
        ```

        :return: json body of the blockchain info
        """
        res = self._get(self._url("/chain"))
        return self._result(res, True)
