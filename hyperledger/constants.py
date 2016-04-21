#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

DEFAULT_API_VERSION = "0.1.0"
DEFAULT_TIMEOUT_SECONDS = 60

DEFAULT_BASE_URL = "http://127.0.0.1:5000"


# Chaincode related values
CHAINCODE_LANG_GO = 1
CHAINCODE_LANG_NODE = 2

CHAINCODE_CONFIDENTIAL_PUB = 0
CHAINCODE_CONFIDENTIAL_CON = 1

DEFAULT_CHAINCODE_METHODS = ['deploy', 'invoke', 'query']
DEFAULT_CHAINCODE_PATH = "github.com/hyperledger/fabric/examples/chaincode" \
                         "/go/chaincode_example02"
DEFAULT_CHAINCODE_INIT_FUNC = "init"
DEFAULT_CHAINCODE_INIT_ARGS = ["a", "10000", "b", "20000"]

DEFAULT_CHAINCODE_CONFIDENTIALITY = 0
