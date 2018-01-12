## gRPC文件生成方式说明

引用了一个第三方库grpclib来支持异步，请先在本目录下执行

``` python
pip install git+https://github.com/vmagamedov/grpclib.git
python -m grpc_tools.protoc -I. --python_out=../ --grpc_python_out=../ --python_grpc_out=../ ./hello.proto
```