#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import json
import hashlib
import random
import time

# Create a directory to store user data
USER_DIR = "users"
if not os.path.exists(USER_DIR):
    os.makedirs(USER_DIR)

def hash_password(password):
    """Hashes the password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    """Registers a new user and saves to a JSON file"""
    username = input("Enter username (max 20 chars): ").strip()
    if len(username) == 0 or len(username) > 20:
        print("❌ Invalid username length!")
        return
    if not username.isalnum():
        print("❌ Username must be alphanumeric!")
        return

    password = input("Enter password (min 6, max 30 chars): ").strip()
    if len(password) < 6 or len(password) > 30:
        print("❌ Password length not allowed!")
        return

    user_file = os.path.join(USER_DIR, f"{username}.json")
    if os.path.exists(user_file):
        print("❌ Username already exists!")
        return

    hashed = hash_password(password)
    with open(user_file, "w") as f:
        json.dump({"username": username, "password": hashed}, f)

    print("Registration successful!")

def login_user():
    """Login function (will be extended in Modules 2 & 3)"""
    username = input("Enter username: ").strip()

    # Check for suspicious characters or trapdoor attempts
    if ".." in username or "/" in username or "\\" in username:
        print("Suspicious username detected!")
        return False

    user_file = os.path.join(USER_DIR, f"{username}.json")
    if not os.path.exists(user_file):
        print("❌ User not found!")
        return False

    if os.path.getsize(user_file) < 20:
        print("Possible tampering detected. File is too small!")
        return False

    with open(user_file, "r") as f:
        user_data = json.load(f)

    password = input("Enter password: ").strip()
    if hash_password(password) != user_data["password"]:
        print("Incorrect password!")
        return False

    # ← Module 2's MFA will go here
        # Step 2: OTP Generation
    otp = str(random.randint(100000, 999999))
    print(f"\n📲 Your OTP is: {otp}")
    otp_valid_until = time.time() + 60  # OTP valid for 60 seconds

    attempts = 3
    while attempts > 0:
        entered_otp = input("Enter OTP: ").strip()
        current_time = time.time()

        if current_time > otp_valid_until:
            print("⏳ OTP expired!")
            return False

        if entered_otp == otp:
            print("MFA successful! You are logged in.")
            return True
        else:
            attempts -= 1
            print(f"❌ Incorrect OTP. Attempts left: {attempts}")

    print("🚫 Too many incorrect attempts. Login failed.")
    return False

    print("Login successful!")  
    return True
    


# In[ ]:


while True:
    print("\nAUTH SYSTEM MENU")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("❌ Invalid choice!")


# In[ ]:




