
from fastapi import FastAPI, WebSocket
import asyncio
from heatmap import analyze

app = FastAPI()

state = {"tick":0,"players":[{"id":1,"x":10,"y":20},{"id":2,"x":50,"y":80}]}

async def loop():
    i=0
    global state
    while True:
        state = {
            "tick": i,
            "players":[
                {"id":1,"x":10+i,"y":20+i},
                {"id":2,"x":50,"y":80-i}
            ]
        }
        i += 1
        await asyncio.sleep(1)

@app.on_event("startup")
async def start():
    asyncio.create_task(loop())

@app.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket.accept()
    while True:
        ai = analyze(state)
        await websocket.send_json({"map":state,"ai":ai})
        await asyncio.sleep(0.5)
