#!/usr/bin/env python
from sanic import Sanic
from sanic.response import text

app = Sanic()


@app.route("/")
async def test(request):
    return text('Hello World!')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
