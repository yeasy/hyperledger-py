#!/usr/bin/env bash

# should be use on the top directory

python -m grpc.tools.protoc -I./protos --python_out=./src/lib --grpc_python_out=./src/lib protos/*.proto