from flask import Flask
from flask import render_template, redirect, url_for, request

import models.liske as liske
import models.task as task
import dal.liske_repository as liske_repository
import dal.task_repository as task_repository

app = Flask("Liske")
liskeList = []

@app.route("/")
def index():
    #TODO: Validar la sesión del usuario
    return redirect(url_for("show_list", selectedLiske = 1))

@app.route("/liske/<selectedLiske>")
def show_list(selectedLiske = 1):
    liske = []
    liske = liske_repository.get_liske_list()

    return render_template("index.html", response=(liske, selectedLiske))


@app.route("/removetask/<id>", methods=["DELETE"])
def remove_task(id):
    is_deleted = False

    if id != None and str(id).isnumeric():
        is_deleted = task_repository.remove_task(id)

    return str(is_deleted)

@app.route("/addtask", methods=["POST"])
def add_task():
    task_liske = request.form["liskeId"]
    task_name = request.form["taskName"]
    task_priority = request.form.get("priority")

    task_repository.add_task(task_liske, task_name, task_priority)

    return redirect(url_for('show_list', selectedLiske = task_liske))

@app.route("/addliske", methods=["POST"])
def add_liske():
    selected_liske = request.form["currentLiske"]
    liske_name = request.form["liskeName"]

    liske_repository.add_liske(liske_name)

    return redirect(url_for('show_list', selectedLiske = selected_liske))

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