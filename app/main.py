from fastapi import FastAPI
from fastapi.responses import JSONResponse

from . import database

app = FastAPI(
    title="OTPless User Analytics API",
    description="Backend API for authentication metrics (signups, retention, etc.) for OTPless platform.",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the OTPless User Analytics API!"}


@app.get("/metrics/signups", summary="Get user signup counts by date")
def signup_counts():
    counts = database.get_signup_counts()
    # Convert pandas Series to dict for JSON response
    return JSONResponse(content=counts.to_dict())


@app.get("/metrics/active-users", summary="Get current count of active users")
def active_users():
    count = len(database.get_active_users())
    return {"active_users": count}


@app.get("/metrics/churned-users", summary="Get current count of churned users")
def churned_users():
    count = len(database.get_churned_users())
    return {"churned_users": count}


@app.get("/metrics/daily-active-users", summary="Get count of users active per day")
def daily_active_users():
    daily_counts = database.get_daily_active_counts()
    return JSONResponse(content=daily_counts.to_dict())
