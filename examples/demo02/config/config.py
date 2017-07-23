#!/usr/bin/env python
import os


class Config():
    """
    Basic config for demo02
    """
    # Application config
    TIMEZONE = 'Asia/Shanghai'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
