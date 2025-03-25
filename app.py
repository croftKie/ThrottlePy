from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
import redis

load_dotenv()

app = FastAPI()

redis_cli = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("PORT"),
    charset="utf-8",
    decode_responses=True
    )
connection = redis_cli.ping()

redis_cli.set("test-key", 1994)
print(redis_cli.get("test-key"))

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
