import dal.db as db
import models.liske as m_liske
import models.task as task

def get_liske_list():
    liske_list = []
    taskList1 = [
            task.task(1, 'Titulo 1', 1),
            task.task(2, 'Titulo 2', 3),
            task.task(3, 'Titulo 3', 2)
        ]

    #TODO: obtener las task por cada liske
    liske = db.query_db("select * from liske")

    for currentLiske in liske:
        liske_list.append(m_liske.liske(currentLiske[0], currentLiske[1], taskList1))

    return liske_list