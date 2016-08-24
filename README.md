# hyperledger-py 

[![Build Status](https://travis-ci.org/yeasy/hyperledger-py.svg?branch=grpc)](https://travis-ci.org/yeasy/hyperledger-py)
[![PyPI Version](http://img.shields.io/pypi/v/hyperledger.svg)](https://pypi.python.org/pypi/hyperledger)

**Currently the project is under reconstruction based on gRPC. To use the legacy restful base one, please switch to the `restful` branch.**

Python SDK client for [Hyperledger](https://github.com/hyperledger/hyperledger).

This project will follow the [Hyperledger SDK Spec](https://github.com/hyperledger/fabric/wiki/Client-SDK-Specification) to let users use those APIs by importing a simple python library.

*If you want a quick start with a hyperledger cluster without any local
configuration and vagrant setup, please use this 
[compose-file](https://github.com/yeasy/docker-compose-files#hyperledger).*

## Installation
The stable version is always available on PyPi.
```sh
$ pip install hyperledger --upgrade
```

The latest version is on [github](https://github.com/yeasy/hyperledger-py).
```sh
$ git clone https://github.com/yeasy/hyperledger-py.git
$ cd hyperledger-py
$ make install
```

## Change Logs
See [change log](docs/change_log.md).

## Documentation
The source is available in the [docs](docs) directory.

* [Design Spec](docs/design.md)

## Testing(TBD)
All testing code is under [tests](tests) directory.

After installation, you can run a quick full-functional testing (deploy,
invoke, query chaincode, etc.) with your hyperledger cluster by

```python
$ python tests/function_test.py HYPERLEDGER_API_URL
```

## Contribution
Please see [Contribution Instruction](docs/contribution.md).

## TODO Items

* Write the api design doc
* Reconstruct based on gRPC

## Acknowledgement

This work is highly inspired by the following projects:

 * [Hyperledger fabric](https://github.com/hyperledger/fabric)

## License

This work is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for full license text.