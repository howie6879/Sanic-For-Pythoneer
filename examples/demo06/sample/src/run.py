# !/usr/bin/env python
import os
import sys

from sanic import Sanic

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.views import api_bp, html_bp, json_bp

app = Sanic(__name__)

app.blueprint(api_bp)
app.blueprint(html_bp)
app.blueprint(json_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
