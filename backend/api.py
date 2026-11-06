from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any

from function_agent import (
    run,
    alxValue,
    bpeEncode,
    cipher,
    decipher,
    gridWalker,
    isBalanced,
    scoreword,
    sortAscending,
    daysToDeadline
)

app = FastAPI(title="My Gemini Agent API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register available functions
function_map = {
    "alxValue": alxValue,
    "bpeEncode": bpeEncode,
    "cipher": cipher,
    "decipher": decipher,
    "gridWalker": gridWalker,
    "isBalanced": isBalanced,
    "scoreword": scoreword,
    "sortAscending": sortAscending,
    "daysToDeadline": daysToDeadline
}


class ChatRequest(BaseModel):
    message: str


class FunctionRequest(BaseModel):
    function: str
    arguments: dict[str, Any]


@app.get("/")
def home():
    return {"message": "Gemini Agent API is running!"}


@app.post("/chat")
def chat(request: ChatRequest):
    response = run(request.message)
    return {"response": response}


@app.post("/functions")
def execute_function(request: FunctionRequest):

    selected_function = function_map.get(request.function)

    if selected_function is None:
        raise HTTPException(
            status_code=404,
            detail="Function not found"
        )

    try:
        result = selected_function(**request.arguments)
        return {"function": request.function, "result": result}

    except TypeError as error:
        raise HTTPException(status_code=400, detail=str(error))
