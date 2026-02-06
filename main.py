from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.database import engine, Base
from app.routers import tasks, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API", version="0.1.0")

app.include_router(auth.router)
app.include_router(tasks.router)


@app.exception_handler(ValueError)
def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})


@app.exception_handler(Exception)
def generic_error_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})


@app.get("/")
def root():
    return {"message": "TaskFlow API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
