import dal.db as db


def check_credentials(user, password):
    cursor = db.query_db("select * from user where user_name = ? and user_password = ? ", (user, password))

    return len(cursor) > 0