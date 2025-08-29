# Tarpaulin API

A robust and scalable backend API developed with Flask, providing secure user authentication and profile management, deployed on Google Cloud Platform.

## 🌐 Live Demo

Explore the live application here: https://tarpaulin-sunto.uw.r.appspot.com/

## 🚀 Project Overview

Tarpaulin API is a RESTful backend service built using Python's Flask framework. It offers secure user authentication, profile management, and integrates with Google Cloud services for scalability and reliability. The API is designed to handle user registration, login, and avatar management, with JWT-based authentication ensuring secure access.

## 🛠️ Features

User Authentication: Secure user registration and login with JWT-based authentication.

Profile Management: Users can update their profile information and upload avatars.

Google Cloud Integration: Deployed on Google Cloud Platform, utilizing services like Secret Manager for secure credential management.

CI/CD Pipeline: Automated testing and deployment using GitHub Actions, ensuring continuous integration and delivery.

## 📁 Project Structure
/tarpaulin-api
├── /app                # Core application logic
├── /api                # API-specific logic and utilities
├── /postman            # Postman collections and environment files for testing
├── main.py             # Entry point for the application
├── requirements.txt    # Python dependencies
└── .github/workflows   # GitHub Actions CI/CD workflows

## ⚙️ Setup and Installation
1. Clone the repository:
```
git clone https://github.com/Tongxin-Sun/tarpaulin-api.git
cd tarpaulin-api
```

2. Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the application:
```
python main.py
```

🧪 Testing

To run Postman tests locally:
```
newman run postman/tarpaulin.postman_collection.json -e postman/tarpaulin.postman_environment.json
```
