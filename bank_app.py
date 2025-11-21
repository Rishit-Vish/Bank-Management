import streamlit as st
import json
import random
import string
from pathlib import Path

class Bank:
    database = 'database.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
    except Exception as err:
        st.error(f"Error loading database: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data))

    @staticmethod
    def __accountno():
        alpha = random.choices(string.ascii_letters, k=5)
        digits = random.choices(string.digits, k=4)
        id = alpha + digits
        random.shuffle(id)
        return "".join(id)

    def createaccount(self, name, email, phone, pin):
        if len(str(pin)) != 4 or len(str(phone)) != 10:
            return "Invalid PIN or Phone Number"

        d = {
            "name": name,
            "email": email,
            "Phone No.": int(phone),
            "PIN": int(pin),
            "Account No.": Bank.__accountno(),
            "Balance": 0
        }
        Bank.data.append(d)
        Bank.__update()
        return d["Account No."]

    def deposit_money(self, accNo, pin, amount):
        user_data = [i for i in Bank.data if str(i['Account No.']) == accNo and str(i["PIN"]) == str(pin)]
        if not user_data:
            return "User not found"
        if amount <= 0 or amount > 10000:
            return "Invalid Amount"
        user_data[0]['Balance'] += amount
        Bank.__update()
        return f"Amount Credited. New Balance: {user_data[0]['Balance']}"

    def withdraw_money(self, accNo, pin, amount):
        user_data = [i for i in Bank.data if str(i['Account No.']) == accNo and str(i["PIN"]) == str(pin)]
        if not user_data:
            return "User not found"
        if amount <= 0 or amount > 10000:
            return "Invalid Amount"
        if user_data[0]['Balance'] < amount:
            return "Insufficient funds"
        user_data[0]['Balance'] -= amount
        Bank.__update()
        return f"Amount Debited. New Balance: {user_data[0]['Balance']}"

    def details(self, accNo, pin):
        user_data = [i for i in Bank.data if str(i['Account No.']) == accNo and str(i["PIN"]) == str(pin)]
        if not user_data:
            return "User not found"
        return user_data[0]

    def update_details(self, accNo, pin, new_data):
        user_data = [i for i in Bank.data if str(i['Account No.']) == accNo and str(i["PIN"]) == str(pin)]
        if not user_data:
            return "User not found"
        for key in ['name', 'email', 'Phone No.', 'PIN']:
            if new_data.get(key):
                if key in ['PIN', 'Phone No.']:
                    user_data[0][key] = int(new_data[key])
                else:
                    user_data[0][key] = new_data[key]
        Bank.__update()
        return "Details updated successfully"

    def deleteaccount(self, accNo, pin):
        user_data = [i for i in Bank.data if str(i['Account No.']) == accNo and str(i["PIN"]) == str(pin)]
        if not user_data:
            return "User not found"
        Bank.data.remove(user_data[0])
        Bank.__update()
        return "Account deleted successfully"


bank = Bank()
st.title("🏦 Bank Management System")

menu = ["Create Account", "Deposit Money", "Withdraw Money", "View Details", "Update Details", "Delete Account"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create Account":
    st.subheader("Create New Account")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    pin = st.text_input("PIN (4 digits)", type="password")
    if st.button("Create Account"):
        acc_no = bank.createaccount(name, email, phone, pin)
        st.success(f"Account created successfully. Your Account Number is: {acc_no}")

elif choice == "Deposit Money":
    st.subheader("Deposit Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Deposit"):
        st.info(bank.deposit_money(acc_no, pin, amount))

elif choice == "Withdraw Money":
    st.subheader("Withdraw Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Withdraw"):
        st.info(bank.withdraw_money(acc_no, pin, amount))

elif choice == "View Details":
    st.subheader("View Account Details")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("View"):
        details = bank.details(acc_no, pin)
        st.json(details)

elif choice == "Update Details":
    st.subheader("Update Account Details")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    new_name = st.text_input("New Name (leave blank to keep same)")
    new_email = st.text_input("New Email (leave blank to keep same)")
    new_phone = st.text_input("New Phone (leave blank to keep same)")
    new_pin = st.text_input("New PIN (leave blank to keep same)", type="password")
    if st.button("Update"):
        new_data = {
            "name": new_name,
            "email": new_email,
            "Phone No.": new_phone,
            "PIN": new_pin
        }
        st.success(bank.update_details(acc_no, pin, new_data))

elif choice == "Delete Account":
    st.subheader("Delete Account")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Delete"):
        st.warning(bank.deleteaccount(acc_no, pin))
