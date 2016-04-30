#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


class NetworkApiMixin(object):

    def peer_list(self):
        """ GET /network/peers

        Use the Network APIs to retrieve information about the network of peer
        nodes comprising the blockchain network.


        ```golang
        message PeersMessage {
            repeated PeerEndpoint peers = 1;
        }
        message PeerEndpoint {
            PeerID ID = 1;
            string address = 2;
            enum Type {
              UNDEFINED = 0;
              VALIDATOR = 1;
              NON_VALIDATOR = 2;
            }
            Type type = 3;
            bytes pkiID = 4;
        }
        message PeerID {
            string name = 1;
        }
        ```

        :return: json body of the network peers info
        """
        res = self._get(self._url("/network/peers"))
        return self._result(res, True)
