import time
from fastapi import FastAPI, Request


from app import app

@app.middleware("http")
async def log_process_time(request: Request, call_next):
    print("hello world!")


