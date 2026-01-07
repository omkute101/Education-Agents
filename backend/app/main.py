import uvicorn
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Education Agent API",
    description="API for Education Agents",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "Initiated..."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
