#!/usr/bin/env python
"""
 Created by howie.hu at  17-10-16.
"""
import grpc
import time

from concurrent import futures

from src.config import CONFIG
from src.grpc_service import hello_pb2, hello_pb2_grpc


GRPC_LISTEN_ADDR = CONFIG.GRPC_LISTEN_ADDR
GRPC_THREAD_POOLS_MAX_WORKERS = CONFIG.GRPC_THREAD_POOLS_MAX_WORKERS
GRPC_SERVER_SLEEP_SECONDS = CONFIG.GRPC_SERVER_SLEEP_SECONDS


class Hello(hello_pb2_grpc.HelloServicer):
    def hello_action(self, request, context):
        data = request.action
        ip = context.peer()
        print(data, ip)
        reply = hello_pb2.HelloResponse(message=data)
        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=GRPC_THREAD_POOLS_MAX_WORKERS))
    hello_pb2_grpc.add_HelloServicer_to_server(Hello(), server)
    server.add_insecure_port(GRPC_LISTEN_ADDR)
    server.start()
    try:
        while True:
            time.sleep(GRPC_SERVER_SLEEP_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
