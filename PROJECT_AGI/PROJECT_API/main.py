from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello! I am your new API."}

@app.get("/square/{number}")
def calculate_square(number: int):
    result = number * number
    return {
        "input": number,
        "output": result,
        "note": "This calculation was done by my Python server"
    }
