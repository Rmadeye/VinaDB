from tkinter import *
from tkinter import filedialog
import subprocess
from src import dock_parser as p, pdbqtdb as db


class frontend:

    def __init__(self):
        window = Tk()
        window.wm_title("Add to Vina database")

        dbmng = db.database()


        def exit_window():
            window.destroy()

        def browse_pdbqt():
            global logfile
            logfile = filedialog.askopenfilename(filetypes=[("Docking reports", "*.pdbqt")])
            print(logfile)
            logprint = Label(window, text=logfile).grid(row=0, column=0)
            window.update()
            return logfile

        def set_sqltablename():
            tablename = tbl.get()
            tablename = str(tablename)
            print(tablename)
            return tablename

        def run():
            dbmng.df2sqlite(p.parser().parse(logfile), str(set_sqltablename()), 'Vina_database.db')
            fileadded = Label(window, text="Database successfully updated").grid(row=1, column=0)

        def open_sqlitebrowser():
            dbbrowser = subprocess.run(["sqlitebrowser"])

        button1 = Button(window, text="Browse logfile", command=browse_pdbqt).grid(row=0, column=2)
        button3 = Button(window, text="Add to Vina database", command=run).grid(row=2, column=2)
        button4 = Button(window, text="Open database browser", command=open_sqlitebrowser).grid(row=3, column=2)
        button5 = Button(window, text="Exit", command=exit_window).grid(row=4, column=2)
        tbl = Entry(window)
        tbl.grid(row=1, column=2)
        ltbl = Label(window, text="Database table name:").grid(row=1, column=1)
        btbl = Button(window, text="OK", command=set_sqltablename).grid(row=1, column=3)

        window.mainloop()
