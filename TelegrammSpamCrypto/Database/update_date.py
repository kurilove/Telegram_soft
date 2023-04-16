import sqlite3 as sq


async def start_data():
    global db, cur

    db = sq.connect("users_spam")
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users_spam(user_id TEXT,username TEXT,spam INTEGER DEFAULT 0)")

    db.commit()
