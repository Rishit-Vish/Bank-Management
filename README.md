<div align="center">

# 🏦 Bank Management System

**A web-based banking application built with Python, Object-Oriented Programming, and a JSON database, focused on safe data handling.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)
![JSON](https://img.shields.io/badge/Database-JSON-000000?logo=json&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Authentication and Data Handling](#-authentication-and-data-handling)
- [Tech Stack](#-tech-stack)
- [Interface](#-interface)
- [Installation and Setup](#-installation-and-setup)
- [Purpose and Learning Outcomes](#-purpose-and-learning-outcomes)
- [Author](#-author)

---

## 📖 Overview

This project is a Bank Management System built with **Python** using **Object-Oriented Programming (OOP)** concepts and a **JSON-based database**.

It focuses on three things: **safe data handling**, **user authentication**, and **core banking operations**.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🆕 **Create Account** | Open a new bank account |
| ✏️ **Update Account Details** | Edit the details of an existing account |
| 🗑️ **Delete Account** | Remove an existing account |
| 💵 **Deposit Money** | Add money to an account |
| 💸 **Withdraw Money** | Take money out of an account |
| 👁️ **View Account Details** | Display the account's information |

---

## 🔐 Authentication and Data Handling

Users are authenticated with their **Account Number + PIN / Password**.

### Safe Update Workflow

To prevent accidental corruption of the database, changes are never written straight to the main file:

```
Authenticate user
      ↓
Copy user data into a temporary structure
      ↓
Perform the operation on the temporary data
      ↓
Validate the result
      ↓
Update the main JSON database
```

| Step | Why it matters |
|---|---|
| Work on a **temporary copy** | The main database stays untouched while an operation is in progress |
| **Validate** before saving | Invalid operations never reach the stored data |
| Write to the **main JSON file last** | Reduces the risk of accidental data corruption |

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python |
| **Programming Paradigm** | Object-Oriented Programming (OOP) |
| **Database** | JSON file |
| **User Interface** | Streamlit |

---

## 🖥️ Interface

The interface is built with **Streamlit** and runs as a **web-based app** in the browser, not only in the terminal.

---

## 🚀 Installation and Setup

### Prerequisites

- Python installed on your system

### 1. Clone the repository

```bash
git clone https://github.com/Rishit-Vish/Bank-Management-System.git
cd Bank-Management-System
```

### 2. Install the required library

```bash
pip install streamlit
```

### 3. Run the app

```bash
streamlit run bank_app.py
```

The app opens in your browser at **http://localhost:8501**.

---

## 🎓 Purpose and Learning Outcomes

I created this project as a learning exercise to understand:

- Object-Oriented Programming in Python
- File handling with JSON
- Safe data updates
- Basic banking logic

---

## 👤 Author

**Rishit Vishwakarma**

🔗 GitHub: [Rishit-Vish](https://github.com/Rishit-Vish)
