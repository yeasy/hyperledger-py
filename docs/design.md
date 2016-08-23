
# Design Spec

Here we discuss the design principle and architecture consideration.

In total, we have several modules:

* Client: The top-level class. Users should mostly use this as the entry point.
* Chain: Represent one chain. Provide Blockchain related operations.
* MemberService: Membership related operations.

## Client

## Chain

* getPeers
* sendTransaction

## MemberService

* registerUser
* deleteEnrollment
* getEnrollment
* getEnrollmentEcert
* getEnrollmentTcert
* getTransaction
