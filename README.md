# Role-Based Access Control (RBAC) System

## Overview
This project implements a secure **Authentication and Authorization** system with **Role-Based Access Control (RBAC)** using Python and Flask. The system ensures that users can access specific resources based on their assigned roles (e.g., Admin, Moderator, User).

---

## Features
- **Secure Authentication**: Users can register, log in, and log out securely.
- **Role-Based Access Control (RBAC)**: Access to endpoints is restricted based on roles.
- **JWT Authentication**: JSON Web Tokens are used for session management.
- **Database Integration**: User credentials and roles are stored securely in a database.
- **Dynamic Role Management**: Easily add or modify roles and permissions.
- **Middleware Enforcement**: Role checks implemented via decorators for clean code.

---

## Requirements
Ensure you have the following installed:
- Python 3.7+
- SQLite (or any database of your choice)

Install required Python libraries:

pip install -r requirements.txt

```bash 
rbac_project/
├── app.py             # Main application file
├── models.py          # Database models for Users and Roles
├── routes/
│   ├── auth.py        # Authentication-related routes (register, login)
│   ├── admin.py       # Admin-specific routes
│   ├── user.py        # General user routes
├── utils/
│   ├── hash.py        # Password hashing utilities
│   ├── jwt.py         # JWT-related utilities
├── migrations/        # Database migrations (if applicable)
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

## Setup Instructions
## Clone the Repository

```git clone https://github.com/yourusername/rbac-system.git
cd rbac-system
```
## Initialize the Database
## Run the following commands to create and initialize the database:

Run the following commands to create and initialize the database:
```
python app.py
The database will be created automatically upon running the app.
```
## Start the Application

python app.py
The application will start on http://127.0.0.1:5000.

## Usage
## Available Roles
Admin: Full access to all resources and administrative features.
Moderator: Access to moderate content.
User: Access to general features.
Sample API Endpoints
Register a User

## http
```
Copy code
POST /register
Content-Type: application/json

{
    "username": "user1",
    "password": "password123",
    "role": "User"
}
Login a User
```

## http
```
POST /login
Content-Type: application/json

{
    "username": "user1",
    "password": "password123"
}
Response:

json
{
    "token": "<JWT_TOKEN>"
}
```
## Access Protected Routes Use the JWT token in the Authorization header:
```
makefile
Copy code
Authorization: Bearer <JWT_TOKEN>
Admin-only Route:
http
Copy code
GET /admin
Moderator-only Route:
http
Copy code
GET /moderator
User Route (any authenticated user):
http
Copy code
GET /user
Testing
Use Postman, curl, or any API client to test the endpoints. Below are some example commands:
```
## Login Example:

```

curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" \
-d '{"username": "admin", "password": "admin123"}'
Access Admin Route:
```
```

curl -X GET http://127.0.0.1:5000/admin -H "Authorization: Bearer <JWT_TOKEN>"
```


