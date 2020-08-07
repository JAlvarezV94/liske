from flask import Flask
from flask import render_template, redirect, url_for

import models.liske as liske
import models.task as task
import dal.liske_repository as liske_repository
import dal.task_repository as task_repository

app = Flask("Liske")
liskeList = []

@app.route("/")
def index(selectedLiske = None):
    liske = []
    liske = liske_repository.get_liske_list()
    
    return render_template("index.html", liske=liske)


@app.route("/removetask/<id>", methods=["DELETE"])
def remove_task(id):
    is_deleted = False

    if id != None and str(id).isnumeric():
        is_deleted = task_repository.remove_task(id)

    print(is_deleted)
    if is_deleted:
        return redirect(url_for('index'))
    else:
        return str(is_deleted)


def __debug_liske_list():
    taskList1 = [
        task.task(1, 'Titulo 1', 1),
        task.task(2, 'Titulo 2', 3),
        task.task(3, 'Titulo 3', 2)
    ]
    liske1 = liske.liske(1, 'home tasks', taskList1)

    taskList2 = [
        task.task(4, 'Titulo 1', 1),
        task.task(5, 'Titulo 2', 3),
        task.task(6, 'Titulo 3', 1)
    ]
    liske2 = liske.liske(2, 'work tasks', taskList2)

    taskList3 = [
        task.task(7, 'Titulo 1', 1),
        task.task(8, 'Titulo 2', 3),
        task.task(9, 'Titulo 3', 1)
    ]
    liske3 = liske.liske(3, 'other tasks', taskList3)
    liskeList = [liske1, liske2, liske3]

    return liskeList