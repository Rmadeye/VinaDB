from tkinter import *
from tkinter import filedialog
import subprocess
from src import dock_parser
from src import pdbqtdb

class Application(Frame):

    def exit_window(self):
        self.quit()

    def browse_pdbqt(self):
        self.logfile = filedialog.askopenfilename(filetypes=[("Docking reports", "*.pdbqt")])
        print(self.logfile)
        logprint = Label(self, text=self.logfile).grid(row=0, column=0)
        self.update()
        return self.logfile

    def set_sqltablename(self):
        tablename = self.tbl.get()
        tablename = str(tablename)
        print(tablename)
        return tablename

    def run(self):
        dbmng = pdbqtdb.database()
        parse = dock_parser.parser()

        logprint = Label(self, text=self.logfile).grid(row=0, column=0)
        self.update()
        dbmng.df2sqlite(parse.parse(self.logfile), str(self.set_sqltablename()), 'Vina_database.db')
        fileadded = Label(self, text="Database successfully updated").grid(row=1, column=0)

    def open_sqlitebrowser(self):
        dbbrowser = subprocess.run(["sqlitebrowser"])

    def create_widgets(self):

        button1 = Button(self, text="Browse logfile", command=self.browse_pdbqt).grid(row=0, column=2)
        button3 = Button(self, text="Add to Vina database", command=self.run).grid(row=2, column=2)
        button4 = Button(self, text="Open database browser", command=self.open_sqlitebrowser).grid(row=3, column=2)
        button5 = Button(self, text="Exit", command=self.exit_window).grid(row=4, column=2)
        self.tbl = Entry(self)
        self.tbl.grid(row=1, column=2)
        self.ltbl = Label(self, text="Database table name:").grid(row=1, column=1)
        self.btbl = Button(self, text="OK", command=self.set_sqltablename).grid(row=1, column=3)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        self.winfo_toplevel().title("Vina-DB")
        self.mainloop()

