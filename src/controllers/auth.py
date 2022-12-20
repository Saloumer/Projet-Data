from src.models.database import Database
import streamlit as st
from src.models.cookie import Cookie
from hashlib import sha256
def login(email, Motdepasse):
    db = Database()
    Motdepasse = sha256(Motdepasse.encode(encoding="utf-32")).hexdigest()
    res = db.execute(f"SELECT * FROM users WHERE email='{email}' and password='{Motdepasse}'").fetchone()

    if res != None:
        c = Cookie("data.json")
        c.update({"Email": res[1], "uid":res[0]})
        return True 
    else:
        return False

def signin (email, Motdepasse):
    db = Database()
    Motdepasse = sha256(Motdepasse.encode(encoding="utf-32")).hexdigest()
    db.execute(f"Insert into users (email, password) values ('{email}', '{Motdepasse}')")
    db.commit()

def logout():
    c = Cookie("data.json")
    c.clean()



