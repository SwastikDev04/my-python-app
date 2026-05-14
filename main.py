from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World! Your EC2 is running Docker."}

@app.get("/status")
def read_status():
    return {
        "status": "Online",
        "department": "Electronics and Communication Engineering",
        "project": "Python Deployment"
    }
