import dal.db as db
import models.liske as m_liske
import models.task as m_task


def add_liske(liske_name):
    print("Nombre del liske" + liske_name)
    db.void_query_db("insert into liske (liske_name) values (?)", (liske_name, ))

def get_liske_by_id(id):
    selected_liske = None

    liske = db.query_db("select * from liske where id_liske = ?", (id,))

    if liske != None:
        for currentLiske in liske:
            tasks = db.query_db("select * from task where task_liske = ?",(currentLiske[0],))
            task_list = []

            for currentTask in tasks:
                task_list.append(m_task.task(currentTask[0], currentTask[1], currentTask[2]))

            selected_liske = m_liske.liske(currentLiske[0], currentLiske[1], task_list[:])

    return selected_liske


def get_liske_list():
    liske_list = []

    liske = db.query_db("select * from liske")

    if liske != None:
        for currentLiske in liske:
            tasks = db.query_db("select * from task where task_liske = ?",(currentLiske[0],))
            task_list = []

            for currentTask in tasks:
                task_list.append(m_task.task(currentTask[0], currentTask[1], currentTask[2]))

            liske_list.append(m_liske.liske(currentLiske[0], currentLiske[1], task_list[:]))


    return liske_list

def remove_liske(id):
    liske_deleted = False

    liske_deleted = db.void_query_db("delete from liske where id_liske = ?", (id,))

    return liske_deleted