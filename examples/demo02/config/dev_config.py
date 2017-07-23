#!/usr/bin/env python
from .config import Config


class DevConfig(Config):
    """
    Dev config for owllook
    """

    # Application config
    DEBUG = True
