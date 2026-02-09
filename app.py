import sqlite3
from flask import Flask, request

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

if __name__ == "__main__":
    app.run()
