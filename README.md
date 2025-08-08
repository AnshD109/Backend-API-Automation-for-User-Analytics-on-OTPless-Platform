# OTPless User Analytics Backend API

A professional, demo-ready backend API for user analytics and authentication metrics, inspired by real-world product analytics at OTPless.

**Tech Stack:**  
FastAPI · Python · Pandas

---

## ✨ Features

- **User Signup Analytics:** Daily signup stats
- **Active User & Churned User Counts**
- **Daily Active Users**
- **Modular and scalable API structure**

---

## 📁 Project Structure

---

## 🚀 How to Run

1. **Clone the repo**

    ```bash
    git clone https://github.com/yourusername/backend-auth-metrics-api-otpless.git
    cd backend-auth-metrics-api-otpless
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Start the server**

    ```bash
    uvicorn app.main:app --reload
    ```

4. **Open in browser:**  
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

   **Interactive API docs:**  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📊 Example API Endpoints

- **GET** `/metrics/signups`  
  → Daily signup counts

- **GET** `/metrics/active-users`  
  → Current number of active users

- **GET** `/metrics/churned-users`  
  → Current number of churned users

- **GET** `/metrics/daily-active-users`  
  → Number of users active each day

---

## 📦 Data

> All user data is simulated/mock for demo purposes only.

- 100 fake users, with `signup_date`, `last_active_date`, and status (`active`/`churned`).
- See: [`data/sample_users.csv`](data/sample_users.csv)

---

## 💡 Why This Project?

- Demonstrates practical backend experience for product analytics
- Shows ability to design, build, and document clean APIs with real business logic
- Ready for recruiter review, portfolio, or coding assignments

---

## 📝 Author

- Ansh Dankhara (https://github.com/AnshD109)
- Inspired by work at OTPless

---

