import sys, os
# Database creation
def df2sqlite(dataframe,tbl_name,db_name="Vina_database.db"):
    import sqlite3
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    wildcards = ','.join(['?'] * len(dataframe.columns))
    tbl_name = [tuple(x) for x in dataframe.values]

    col_str = '"' + '","'.join(dataframe.columns) + '"'
    cur.execute("create table IF NOT EXISTS %s (%s)" % (tbl_name, col_str))
    cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), tbl_name)

    cur.execute("DELETE FROM tbl_name WHERE rowid NOT IN (SELECT min(rowid) FROM tbl_name GROUP BY Filename,RMSDBestMode)")

    conn.commit()
    conn.close()

