from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
import redis
from redis_state import Redis_state

load_dotenv()

app = FastAPI()

redis_state = Redis_state("localhost", 6379)

redis_state._test_connection()

@app.middleware("http")
async def rate_limiter(request: Request, call_next):
    response = await call_next(request)
    print("hello world!")
    return response

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


@app.get("/data", tags=["Data"])
async def read_root():
    return {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "city": "New York",
    "hobbies": ["reading", "cycling", "coding"]
}




# Utilities
