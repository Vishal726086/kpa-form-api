# KPA Form Data API - Vishal

This project implements two backend APIs from the [KPA Form Data Postman collection](https://kpa.suvidhaen.com), using **FastAPI** and **PostgreSQL**. The APIs allow submitting and retrieving KPA form data entries and are fully compatible with the given frontend and request/response structure.

---

## 📌 Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Server**: Uvicorn
- **Tools**: Postman for testing, .env for configuration

---

## 🚀 Setup Instructions

1. **Clone the repository or unzip the folder**

2. **Create virtual environment & activate**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Create a .env file in the root directory:**
DATABASE_URL=postgresql://postgres:<your_password>@localhost:5432/kpa_db

5. **Run the server**
uvicorn app.main:app --reload

6. **Access API Docs (Swagger UI)**
Open browser and go to:
http://127.0.0.1:8000/docs



## ✅ Implemented APIs

1. **POST /form-data/submit**
Description: Submit KPA form details

Request Body (JSON):
{
  "name": "Vishal Anand",
  "phone_number": "7760873976",
  "district": "Bhopal",
  "block": "Block A",
  "village": "Village X",
  "address": "123 Some Address",
  "category": "General",
  "sub_category": "SubA",
  "occupation": "Student",
  "organization": "ABC NGO"
}

Response:
{
  "name": "Vishal Anand",
  "phone_number": "7760873976",
  "district": "Bhopal",
  "block": "Block A",
  "village": "Village X",
  "address": "123 Some Address",
  "category": "General",
  "sub_category": "SubA",
  "occupation": "Student",
  "organization": "ABC NGO",
  "id": 3
}

2. **GET /form-data/{id}**
Description: Fetch a single form data entry by ID

Example: GET /form-data/3

Response:
{
  "name": "Vishal Anand",
  "phone_number": "7760873976",
  "district": "Bhopal",
  "block": "Block A",
  "village": "Village X",
  "address": "123 Some Address",
  "category": "General",
  "sub_category": "SubA",
  "occupation": "Student",
  "organization": "ABC NGO",
  "id": 3
}


## 🧪 Testing
Use Postman or Swagger UI (/docs) to test endpoints.

A sample Postman collection is included:
KPA Form Data - Vishal.postman_collection.json


## 📝 Assumptions / Notes
Only two endpoints were implemented as per assignment instructions.

FastAPI auto-generates Swagger UI at /docs for testing and debugging.

The ID is auto-incremented by the database.


## 📁 Folder Structure
app/
│
├── main.py               # FastAPI app instance
├── database.py           # DB connection
├── models.py             # SQLAlchemy models
├── schemas.py            # Pydantic schemas
└── routers/
    └── form_data.py      # API route handlers

---

## 🙋‍♂️ Submitted by:
Vishal Kumar
MCA Fresher | Python & Django Developer
