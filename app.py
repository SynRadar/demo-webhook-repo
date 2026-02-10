import sqlite3
from flask import Flask, request
import os

app = Flask(__name__)

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

@app.route("/poplpop")
def demo():
    return f"Demo Function"

if __name__ == "__main__":
    app.run()
