from fastapi import FastAPI

app = FastAPI(title="FastAPI Docker Example", version="1.0.0")


@app.get("/")
def read_root():
    """Root endpoint — returns a greeting."""
    return {"message": "Hello, FastAPI on Docker!"}


@app.get("/health")
def health_check():
    """Health-check endpoint for container orchestrators."""
    return {"status": "ok"}
