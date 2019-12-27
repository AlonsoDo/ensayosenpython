#!/usr/bin/env python
# -*- coding: utf-8 -*-

#self.raiz.title("DataStock")
#self.raiz.resizable(0,0)

from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry


class DataStock(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("DataStock")
        self.master.resizable(0,0)
        self.pack(fill=BOTH, expand=True)

        Tablero = Frame(self)
        Tablero.pack(fill=X)

        lbl1 = Label(Tablero, text="Title", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(Tablero)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Author", width=6)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)


def main():

    root = Tk()
    root.geometry("300x300+300+300")
    app = DataStock()
    root.mainloop()


if __name__ == '__main__':
    main()
    
    