Multi-factor Authentication (MFA) System with User Registration and Login

This project implements a secure authentication system with Multi-factor Authentication (MFA) using Python. The system features a simple command-line interface for user registration, login, and additional security through OTP (One-Time Password) verification.

Features:
- User Registration: Allows users to register with a unique alphanumeric username and password. The password is securely hashed using SHA-256 before being stored in a JSON file.

- User Login: Users can log in using their username and password. Upon successful login, an OTP (One-Time Password) is generated and sent for additional authentication.

- Multi-factor Authentication (MFA): After successful login with the correct credentials, users are prompted to enter a 6-digit OTP that expires after 60 seconds.

Security Features:

- Passwords are securely stored using SHA-256 hashing.

- Input sanitization prevents common attack vectors, such as path traversal and suspicious input.

- Basic file integrity checks to detect potential tampering with stored user data.

Technologies Used:

- Python: The authentication logic is implemented using Python.

- SHA-256: A cryptographic hash function used to securely store passwords.

- JSON: User data (username and hashed password) is stored locally in JSON files.

- Random & Time: Used to generate OTPs and manage OTP expiration.

Requirements:

Python 3.x

How to Run:

1. Clone this repository to your local machine.

2. Ensure Python 3.x is installed.

3. Run python app.py in the command line to start the authentication system.

4. Register a new user, log in using your credentials, and enter the OTP to successfully log in.

Future Improvements:

1. Adding features like password reset and user session management.

2. Using a database (e.g., SQLite) for persistent data storage instead of JSON files.

3. Support for email or SMS-based OTP delivery for more secure multi-factor authentication.

