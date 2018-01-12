#!/usr/bin/env python
import os

from .config import Config


class DevConfig(Config):
    # Application config
    DEBUG = True
    AUTH = {
        "Api-Key": os.getenv('OWLLOOK_API_KEY', "1167c19cd0546a82fbc534f5e93423d5")
    }

    # Redis config
    REDIS_DICT = dict(
        IS_CACHE=True,
        REDIS_ENDPOINT=os.getenv('REDIS_ENDPOINT', "localhost"),
        REDIS_PORT=os.getenv('REDIS_PORT', 6379),
        REDIS_PASSWORD=os.getenv('REDIS_PASSWORD', None),
        DB=0,
        POOLSIZE=10,
    )

    # gRPC config
    GRPC_LISTEN_ADDR = "0.0.0.0:8990"
    GRPC_SERVER_SLEEP_SECONDS = 60 * 60 * 24
    GRPC_THREAD_POOLS_MAX_WORKERS = 1024
