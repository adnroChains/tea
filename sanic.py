from sanic import Sanic
from sanic.response import json, text

app = Sanic("MySanicServer")

@app.get("/")
async def root(request):
    return text("Sanic сервер работает!")

@app.get("/api/info")
async def info(request):
    return json({"status": "ok", "data": "Пример Sanic API"})

@app.post("/api/echo")
async def echo(request):
    data = request.json
    return json({"you_sent": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
