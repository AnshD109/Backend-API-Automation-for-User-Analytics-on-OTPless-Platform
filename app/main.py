from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="OTPless User Analytics API",
    description="Backend API for authentication metrics (signups, retention, etc.) for OTPless platform.",
    version="1.0.0",
)

# --- Sample root endpoint ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the OTPless User Analytics API!"}
