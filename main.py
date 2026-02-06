from fastapi import FastAPI

app = FastAPI(title="TaskFlow API", version="0.1.0")


@app.get("/")
def root():
    return {"message": "TaskFlow API is running"}
