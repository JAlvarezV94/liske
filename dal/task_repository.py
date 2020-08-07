import dal.db as db
import models.task as m_task


def remove_task(id):
    liske_deleted = False
    print(id)
    liske_deleted = db.void_query_db("delete from task where id_task = ?", (id,))
    print(liske_deleted)
    return liske_deleted