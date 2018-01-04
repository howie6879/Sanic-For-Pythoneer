# !/usr/bin/env python
import sys

from sanic import Sanic

sys.path.append('../')
from src.views import json_bp, html_bp

app = Sanic(__name__)
app.blueprint(json_bp)
app.blueprint(html_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
