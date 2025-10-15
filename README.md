# rtsp-overlay-backend

# RTSP Overlay App

This repository contains the **RTSP Overlay App**, including:

- **Backend:** FastAPI + MongoDB for CRUD APIs for overlays  
- **Frontend:** React.js for overlay management UI  

---

## 🔹 Features

- Create, Read, Update, Delete overlays
- FastAPI backend with automatic Swagger docs
- MongoDB for data storage
- React frontend with Axios for API requests
- CORS enabled to allow frontend/backend communication

---

## 🔹 Requirements

- Python 3.9+ (for backend)  
- Node.js + npm/yarn (for frontend)  
- MongoDB (local or remote)  
- pip packages (see `requirements.txt` in backend)

---

## 🔹 Backend Setup (FastAPI)

1. **Clone the repository**

```bash
git clone https://github.com/SaiDwaraka123/rtsp-overlay-backend.git
cd rtsp-overlay-backend
Create a virtual environment

bash
Copy code
python -m venv venv
Activate the virtual environment

Windows (PowerShell)

powershell
Copy code
.\venv\Scripts\activate
Linux / Mac

bash
Copy code
source venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Configure environment variables

Create a .env file in the backend folder:

ini
Copy code
MONGO_URI=mongodb://localhost:27017/
PORT=8000
Run the backend

bash
Copy code
uvicorn main:app --reload
Test the API

Open in browser: http://127.0.0.1:8000/docs

You can test all endpoints (GET, POST, PUT, DELETE).

🔹 Frontend Setup (React.js)
Navigate to the frontend folder:

bash
Copy code
cd path/to/frontend
Install dependencies:

bash
Copy code
npm install
Create .env file in the frontend folder:

ini
Copy code
REACT_APP_API_BASE=http://localhost:8000
Start the React frontend:

bash
Copy code
npm start
The app will open at http://localhost:3000

It communicates with the backend API running on port 8000.

🔹 Project Structure
bash
Copy code
rtsp-overlay-app/
├─ backend/       # FastAPI backend
│  ├─ main.py
│  ├─ requirements.txt
│  └─ .env
├─ frontend/      # React frontend
│  ├─ src/
│  │  ├─ api.js
│  │  └─ OverlayEditor.jsx
│  └─ .env
└─ README.md
