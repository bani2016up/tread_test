from fastapi import FastAPI
import time
from threading import get_native_id

app = FastAPI()


@app.get("/")
def root():
    time.sleep(2)
    thread = get_native_id()
    return {"message": "Hello World", "tread": f"current thread - {thread}"}
