# !/usr/bin/env python
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.views import app
from src.config import CONFIG

app.static('/static', CONFIG.BASE_DIR + '/static')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
