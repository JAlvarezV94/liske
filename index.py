from flask import Flask
from flask import render_template

import models.liske as liske
import models.task as task

app = Flask("Liske")

@app.route("/")
def index(selectedLiske = None):
    
    liskeList = __debug_liske_list()

    return render_template("index.html", liske=liskeList)


def __debug_liske_list():
    taskList1 = [
        task.task('Titulo 1', 1),
        task.task('Titulo 2', 3),
        task.task('Titulo 3', 2)
    ]
    liske1 = liske.liske(1, 'home tasks', taskList1)

    taskList2 = [
        task.task('Titulo 1', 1),
        task.task('Titulo 2', 3),
        task.task('Titulo 3', 1)
    ]
    liske2 = liske.liske(2, 'work tasks', taskList2)

    taskList3 = [
        task.task('Titulo 1', 1),
        task.task('Titulo 2', 3),
        task.task('Titulo 3', 1)
    ]
    liske3 = liske.liske(3, 'other tasks', taskList3)

    return [liske1, liske2, liske3]