from flask import Flask, request
import sqlite3
import subprocess

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Tyrone SAST Lab</h1>
    <p>Proyecto de laboratorio para demostrar SAST con Semgrep.</p>
    <p>Endpoints: /user?username=... y /ping?ip=...</p>
    """


@app.route("/user")
def user():
    username = request.args.get("username", "")

    connection = sqlite3.connect("users.db")

    # VULNERABILIDAD INTENCIONAL: SQL Injection
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    result = connection.execute(query).fetchall()

    connection.close()
    return str(result)


@app.route("/ping")
def ping():
    ip = request.args.get("ip", "")

    # VULNERABILIDAD INTENCIONAL: Command Injection
    result = subprocess.check_output("ping " + ip, shell=True)

    return result.decode()


if __name__ == "__main__":
    app.run(debug=True)
