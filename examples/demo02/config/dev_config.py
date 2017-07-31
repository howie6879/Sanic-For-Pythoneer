#!/usr/bin/env python
from .config import Config


class DevConfig(Config):
    """
    Dev config for demo02
    """

    # Application config
    DEBUG = True
