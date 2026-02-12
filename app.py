import sqlite3
from flask import Flask, request
import os

app = Flask(__name__)

AWS_SECRET_ACCESS_KEY = "AKIA1234567890SECRET"


print("hello duniya")
def greet(name):
    return f"Hello, {name}!"
print("over")
print("test2132")
print("test999")

@app.route("/user")
def get_user():
    user_id = request.args.get("id", "")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return str(cursor.fetchall())

@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    os.system(cmd)
    return "done"

@app.route("/greet")
def greet():
    return "Hello Kon"

@app.route("/zxcvbjuy")
def demo():
    return f"push"

import os

def list_files(path):
    # ❌ Command injection
    os.system("ls " + path)


print("sdfghjkpl[retyghjkl;'uhsdsoifhdi]")

def test_email():
    return f"test email"

if __name__ == "__main__":
    app.run()
