from src.models.database import Database
import streamlit as st
def login(email, Motdepasse):
    db = Database()
    res = db.execute(f"SELECT * FROM users WHERE email='{email}' and password='{Motdepasse}'")
    records = res.fetchall()

    if len(records) > 0:
        return True
    else:
        return False