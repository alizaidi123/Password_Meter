import random
import string

import streamlit as stl
import random as rd
import string as str
import re

def password_strength(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score+=1
    else:
        feedback.append("Password should have at-least 8 characters")
    if re.search(r'[A-Z]', password):
        score+=1
    else:
        feedback.append("Password should have at-least one Upper-Case Alphabet")
    if re.search(r'[a-z]', password):
        score+=1
    else:
        feedback.append("Password should have at-least one Lower-Case Alphabet")
    if re.search(r'[0-9]',password):
        score+=1
    else:
        feedback.append("Password should have at-least one Number")
    if re.search(r'[!@#$%^&*]',password):
        score+=1
    else:
        feedback.append("Password should have at-least one Special Character")

    if score <=2:
        strength = "Weak"
    elif score <=4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength , feedback

def suggest_password():
    char = str.ascii_letters + str.digits + "!@#$%^&*"
    return ''.join(random.choice(char)for _ in  range(12))

stl.title("Password Strength Meter")
password = stl.text_input("Enter Your Password", type="password")
com_password = ["password","1234567890","012345678", "0123456789", "12345678",
                "qwerty", "admin", "letmein","admin123","123password","password123",
                "Password123","Qwerty"]

if password:
    strength,feedback = password_strength(password)
    stl.write(f"Password Strength: **{strength}**")
    if strength in ["Strong", "Moderate"] and password in com_password:
        stl.error("This password is too common. Please choose a stronger one")
    else:
        if strength == "Weak":
            stl.warning("Your password is weak. Please improve it.")
            for suggestions in feedback:
                stl.write(f"-{suggestions}")
        elif strength == "Moderate":
            stl.warning("Your password is moderate. Consider improving it for better security.")
            for suggestions in feedback:
                stl.write(f"-{suggestions}")
        else:
            stl.success("Your password is strong!")

stl.header("Password Suggestion")
if stl.button("Suggest a Strong Password"):
    stg_password = suggest_password()
    stl.write(f" Suggested Password for You {stg_password}")








