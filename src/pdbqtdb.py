import sys, os
# Database creation

class database:

    def df2sqlite(self, dataframe,tbl_name,db_name="Vina_database.db"):
        import sqlite3
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        wildcards = ','.join(['?'] * len(dataframe.columns))
        data = [tuple(x) for x in dataframe.values]

        col_str = '"' + '","'.join(dataframe.columns) + '"'
        cur.execute("create table IF NOT EXISTS %s (%s)" % (tbl_name, col_str))
        cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), data)


        conn.commit()
        conn.close()

