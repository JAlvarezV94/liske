import dal.db as db
import models.task as m_task


def add_task(liske, name, priority):
    db.void_query_db("insert into task (task_name, task_priority, task_liske) values (?, ?, ?)", (name, priority, liske))

def remove_task(id):
    liske_deleted = False
    liske_deleted = db.void_query_db("delete from task where id_task = ?", (id,))
    return liske_deleted