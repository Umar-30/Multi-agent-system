from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.coordinator import Coordinator
import uvicorn

app = FastAPI(title="Multi-Agent System API")
coordinator = Coordinator()

class TaskRequest(BaseModel):
    task: str

class TaskResponse(BaseModel):
    result: str

@app.get("/")
async def root():
    return {"message": "Multi-Agent System API is running"}

@app.post("/execute", response_model=TaskResponse)
async def execute_task(request: TaskRequest):
    try:
        result = coordinator.execute(request.task)
        return TaskResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
