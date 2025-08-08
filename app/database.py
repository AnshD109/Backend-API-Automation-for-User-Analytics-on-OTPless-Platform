import pandas as pd
from pathlib import Path

# Path to the sample data CSV
DATA_PATH = Path(__file__).parent.parent / "data" / "sample_users.csv"

# Read and cache the data (as DataFrame)
def load_user_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["signup_date", "last_active_date"])
    return df

# Example functions to get data slices
def get_all_users():
    df = load_user_data()
    return df

def get_active_users():
    df = load_user_data()
    return df[df["status"] == "active"]

def get_churned_users():
    df = load_user_data()
    return df[df["status"] == "churned"]

def get_signup_counts():
    df = load_user_data()
    return df["signup_date"].value_counts().sort_index()

def get_daily_active_counts():
    df = load_user_data()
    return df.groupby("last_active_date")["user_id"].count()
