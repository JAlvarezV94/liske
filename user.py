from flask import Flask
from flask import render_template, redirect, url_for, request

import helpers.hash_helper as hash_helper
import dal.user_repository as user_repository

app = Flask("Liske")


@app.route("/login")
def login():
    # Get the credentials
    # user = request.form["user"]
    # password = request.form["password"]

    user = "jnoma"
    password = "pass123"

    if user == None or password == None:
        return "nope."

    # Apply the cryp to the pass
    crypted_pass = hash_helper.encrypt_text(password)

    # Check the credentials
    credentials_ok = user_repository.check_credentials(user, crypted_pass)

    return "Logged" if credentials_ok else "Fail!"