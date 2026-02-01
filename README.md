A Bank Management system built using **python (OOPS concept)** with a **JSON-based database**.
The project focuses on safe data handling, authentication and banking operations.

## Features
- Create a new Bank Account.
- Delete an existing Account.
- Update Account Details.
- Deposit Money.
- Withdraw Money.
- View Account Details.

## Authentication & Data Handling
- User is authenticated using **Account Number + PIN/ Password**
- The JSON file is used as a **databse**.
- After authentication, user data is copied into a **temporary structure**.
- All operations are firstly performed on temporary data .
- Only after validation, the main JSON database is updated.
  (prevents accidental corruption of the databse)

## Technologies used - 
- Python
- Object Oriented Programming (OOPS)
- JSON (as database)
- Streamlit (for UI)

## Interface 
- Built using **streamlit**. 
- Runs as a web-based app (not terminal-only)

## Purpose
This project was created as part of a learning exercise to understand:
- OOPS in python.
- File handling with JSON.
- Secure data updates.
- Basic banking logic.
