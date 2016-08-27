
# Design Spec

Here we discuss the design principle and architecture consideration.

In total, we have several modules:

* Client: The top-level class. Users should mostly use this as the entry point.
* Chain: Represent one chain. Provide Blockchain related operations.
* MemberService: Membership related operations.

## Client

* new_chain()            //create a new chain
* get_chain()            //get a chain 
* process_keyvalue()     //store or change persistent and private date
* get_memberservices()   //interact with module MemberService
* member_register()      //register a user
* member_enroll()        //enrollment
* get_chainservices()    //interact with module Chain
* chain_deploy()         //deploy  chaincode
* chain_invoke           // invoke chaincode
* chain_query()          //query chaincode

## Chain

* add_peer()                   //add peer on a chain
* get_peers()                  //get peers of a chain
* get_status()                 //get chain statue
* deploy_transaction()         //implement deploy
* invoke_transaction()         //implement invoke
* query_transaction()          //implement query
* send_transaction()           //send a transaction to peer
* member()                     //interact with MemberService

## MemberService

* get_name()       //Get member name
* register_user()  //Implement register
* is_registered()  //Determine if this name has been registered
* enroll()         //Implement enroll
* is_enrolled()    //Determine if this name has been enrolled
* delete_enrollment() //delete member
* get_enrollment()    //get member info
* get_enrollment_ecert()//enrollment certificates for enroll
* get_enrollment_tcert()//use for transaction,there is a one-to-one relationship between TCert and Transaction
* get_transaction()     //get a transaction from member
* process_confidentiality() // process some security and identity info




## Reference

[Node.js SDK](http://169.53.62.117/site/Setup/NodeSDK-setup/)
