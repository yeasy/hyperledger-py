#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


class RegistrarApiMixin(object):
    def enrollmentID_get(self, enrollment_id):
        """ GET /registrar/{enrollmentID}

        Use the Registrar APIs to manage end user registration with the CA.
        ```golang
        message Block {
            uint32 version = 1;
            google.protobuf.Timestamp Timestamp = 2;
            repeated Transaction transactions = 3;
            bytes stateHash = 4;
            bytes previousBlockHash = 5;
        }
        ```

        :param enrollment_id: The id of the enrollment to retrieve
        :return: json body of the enrollmentID info
        """
        res = self._get(self._url("/registrar/{0}", enrollment_id))
        return self._result(res, True)
