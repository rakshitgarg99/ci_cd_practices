

## fast api code for  hello world

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World!. How are yoou?"}
