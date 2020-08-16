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
def show_list(selectedLiske = None):
    liske_list = []
    selected_liske = None


    # Get the liske id - name list for the menu
    liske_list = liske_repository.get_liske_list()

    # Get the selected Liske complete, if there is not selected then choose the first one.
    if liske_list != None and len(liske_list) > 0:
        liske_id = selectedLiske if selectedLiske != None else liske_list[0].id

        selected_liske = liske_repository.get_liske_by_id(liske_id)


    return render_template("index.html", response=(liske_list, selected_liske))


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

    print(task_liske)
    print(task_name)
    print(task_priority)

    task_repository.add_task(task_liske, task_name, task_priority)

    return redirect(url_for('show_list', selectedLiske = task_liske))

@app.route("/addliske", methods=["POST"])
def add_liske():
    selected_liske = request.form["currentLiske"]
    liske_name = request.form["liskeName"]

    liske_repository.add_liske(liske_name)

    return redirect(url_for('show_list', selectedLiske = selected_liske))