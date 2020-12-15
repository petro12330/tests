import sqlite3

def item_base(value):
    pass
    # name = ''
    # conn = sqlite3.connect(name+'.db')
    # cur = conn.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS pairs(
    #         id integer AUTO_INCREMENT,
    #        caterogy TEXT,
    #        region TEXT);
    #        count INT,
    #        time TEXT
    #     """)

def write(category, region):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS pairs(
        id integer AUTO_INCREMENT,
       caterogy TEXT,
       region TEXT);
    """)
    cur.execute("INSERT INTO pairs(caterogy, region) VALUES(?, ?)", (str(category),str(region)))
    cur.execute("SELECT last_insert_rowid()")
    id = cur.fetchall()[0][0]
    conn.commit()
    return id


def get_pair(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    sql = "SELECT * FROM pairs WHERE id=?"
    cur.execute(sql, [id])
    pair = cur.fetchall()[0][1:3]
    conn.close()
    return pair

