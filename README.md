# hyperledger-py 

[![Build Status](https://travis-ci.org/yeasy/hyperledger-py.svg?branch=master)](https://travis-ci.org/yeasy/hyperledger-py)
[![PyPI Version](http://img.shields.io/pypi/v/hyperledger.svg)](https://pypi.python.org/pypi/hyperledger)

Python client for [Hyperledger](https://github.com/hyperledger/hyperledger).

This project will follow the [Hyperledger API](https://github.com/hyperledger/fabric/tree/master/docs/API) to let uses use those APIs by import a simple python library.

If you want a quick start with a hyperledger cluster without any local 
configuration and vagrant setup, please use this 
[compose-file](https://github.com/yeasy/docker-compose-files#hyperledger).

## Installation
The latest stable version is always available on PyPi.
```sh
$ pip install hyperledger --upgrade
```

The latest `dev` version is on [github](https://github.com/yeasy/hyperledger-py).
```sh
$ git clone https://github.com/yeasy/hyperledger-py.git
$ cd hyperledger-py
$ python setup.py install
```

## Change Logs
See [change log](docs/change_log.md).

## Documentation
The source is available in the `docs/` directory.

* [API Usage](docs/api.md)

## Contribution
Please see [Contribution](CONTRIBUTION.md) and [Contribution 
Instruction](docs/contribution.md).

## Acknowledgement

This work is highly inspired by the following projects:

 * [Hyperledger](https://github.com/hyperledger/hyperledger)
 * [requests](https://pypi.python.org/pypi/requests)
 * [docker-py](https://github.com/docker/docker-py)

## License

This work is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for full license text.
