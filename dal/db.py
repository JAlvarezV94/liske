import sqlite3
from flask import Flask
from flask import g

import os

app = Flask("Liske")

directoryPath = os.path.dirname(__file__)
DATABASE = os.path.join(directoryPath, 'liske.db')


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    rv = None

    try:
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
    except:
        # TODO: Añadir un logger aqui
        rv = None

    return (rv[0] if rv else None) if one else rv

def void_query_db(query, args=()):
    deletion_ok = False

    try:
        db = get_db()
        db.execute(query, args)
        db.commit()
        deletion_ok = True
    except:
        # TODO: Añadir log aquí
        deletion_ok = False

    return deletion_ok