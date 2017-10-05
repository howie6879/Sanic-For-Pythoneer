#!/usr/bin/env python
from .config import Config


class DevConfig(Config):
    # Application config
    DEBUG = True
