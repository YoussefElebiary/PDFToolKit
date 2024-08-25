"""
# Name           :    PDFToolKit
# Description    :    This is a simple program to modify PDF files
# Author         :    Youssef Elebiary - https://github.com/YoussefElebiary
# Version        :    1.0
# File           :    main.py
"""

# =====Imports===== #
from customtkinter import *
from tkinter import messagebox
from os import path, access, R_OK
import functions
#####################


# ====MainClass==== #
class PDFToolKit(CTk):
    def __init__(self):
        super().__init__()
        # Main GUI
        self.title("PDFToolKit")
        self.geometry("300x250")
        self.resizable(False, False)
        self.iconbitmap("./icon.ico")
        # Main Frame
        self.main_f = CTkFrame(self)
        self.main_f.pack(fill=BOTH, expand=1)
        split_b = CTkButton(self.main_f, width=110, height=40, text="Split", command=self.main2split)
        split_b.pack(side=TOP, pady=10)
        merge_b = CTkButton(self.main_f, width=110, height=40, text="Merge", command=self.main2merge)
        merge_b.pack(side=TOP, pady=10)
        extract_b = CTkButton(self.main_f, width=110, height=40, text="Extract", command=self.main2extract)
        extract_b.pack(side=TOP, pady=10)
        insert_b = CTkButton(self.main_f, width=110, height=40, text="Insert", command=self.main2insert)
        insert_b.pack(side=TOP, pady=10)
        # Variables
        self.split_f = None
        self.merge_f = None
        self.extract_f = None
        self.insert_f = None
        self.entry_s = None
        self.entry_e = None
        self.entry_i = None
        self.f_path1 = ""
        self.f_path2 = ""

    def main2split(self):
        self.main_f.pack_forget()
        self.split_f = CTkFrame(self)
        self.split_f.pack(fill=BOTH, expand=1)
        self.title("PDFToolKit - Split")
        back = CTkButton(self.split_f, text="←", width=5, height=5, corner_radius=0, fg_color="red",
                         hover_color="darkred", command=self.split2main)
        back.place(x=0, y=0)
        lbl = CTkLabel(self.split_f, text="File Path", width=30, height=15, font=("bold", 20))
        lbl.place(x=10, y=25)
        get_path = CTkButton(self.split_f, text="Browse", width=140, height=25,
                             font=("bold", 18), command=lambda: self.browse(1))
        get_path.place(x=150, y=25)
        # self.base_name1 = CTkLabel(self.split_f, text="", width=30, height=15, font=("", 11))
        # self.base_name1.place(x=10, y=37)
        lbl2 = CTkLabel(self.split_f, text="Page to split at", width=30, height=15, font=("bold", 18))
        lbl2.place(x=10, y=80)
        self.entry_s = CTkEntry(self.split_f, width=140, height=15)
        self.entry_s.place(x=150, y=80)
        split = CTkButton(self.split_f, text="Split", width=200, height=55,
                          font=("bold", 22), command=self.split_wrapper)
        split.pack(side=BOTTOM, pady=20)

    def split2main(self):
        self.split_f.pack_forget()
        self.main_f.pack(fill=BOTH, expand=1)

    def main2merge(self):
        self.main_f.pack_forget()
        self.merge_f = CTkFrame(self)
        self.merge_f.pack(fill=BOTH, expand=1)
        self.title("PDFToolKit - Merge")
        back = CTkButton(self.merge_f, text="←", width=5, height=5, corner_radius=0, fg_color="red",
                         hover_color="darkred", command=self.merge2main)
        back.place(x=0, y=0)
        lbl = CTkLabel(self.merge_f, text="File 1", width=30, height=15, font=("bold", 20))
        lbl.place(x=10, y=25)
        get_path1 = CTkButton(self.merge_f, text="Browse", width=140, height=25,
                              font=("bold", 18), command=lambda: self.browse(1))
        get_path1.place(x=150, y=25)
        # self.base_name1 = CTkLabel(self.merge_f, text="", width=30, height=15, font=("", 11))
        # self.base_name1.place(x=10, y=37)
        lbl2 = CTkLabel(self.merge_f, text="File 2", width=30, height=15, font=("bold", 20))
        lbl2.place(x=10, y=80)
        # self.base_name2 = CTkLabel(self.merge_f, text="", width=30, height=15, font=("", 11))
        # self.base_name2.place(x=10, y=92)
        get_path2 = CTkButton(self.merge_f, text="Browse", width=140, height=25,
                              font=("bold", 18), command=lambda: self.browse(2))
        get_path2.place(x=150, y=80)
        merge = CTkButton(self.merge_f, text="Merge", width=200, height=55, font=("bold", 22),
                          command=lambda: functions.merge(self.f_path1, self.f_path2))
        merge.pack(side=BOTTOM, pady=20)

    def merge2main(self):
        self.merge_f.pack_forget()
        self.main_f.pack(fill=BOTH, expand=1)

    def main2extract(self):
        self.main_f.pack_forget()
        self.extract_f = CTkFrame(self)
        self.extract_f.pack(fill=BOTH, expand=1)
        self.title("PDFToolKit - Extract")
        back = CTkButton(self.extract_f, text="←", width=5, height=5, corner_radius=0, fg_color="red",
                         hover_color="darkred", command=self.extract2main)
        back.place(x=0, y=0)
        lbl = CTkLabel(self.extract_f, text="File Path", width=30, height=15, font=("bold", 20))
        lbl.place(x=10, y=25)
        get_path = CTkButton(self.extract_f, text="Browse", width=140, height=25,
                             font=("bold", 18), command=lambda: self.browse(1))
        get_path.place(x=150, y=25)
        # self.base_name1 = CTkLabel(self.extract_f, text="", width=30, height=15, font=("", 11))
        # self.base_name1.place(x=10, y=37)
        lbl2 = CTkLabel(self.extract_f, text="Page to extract", width=30, height=15, font=("bold", 18))
        lbl2.place(x=10, y=80)
        self.entry_e = CTkEntry(self.extract_f, width=140, height=15)
        self.entry_e.place(x=150, y=80)
        extract = CTkButton(self.extract_f, text="Extract", width=200, height=55,
                            font=("bold", 22), command=self.extract_wrapper)
        extract.pack(side=BOTTOM, pady=20)

    def extract2main(self):
        self.extract_f.pack_forget()
        self.main_f.pack(fill=BOTH, expand=1)

    def main2insert(self):
        self.main_f.pack_forget()
        self.insert_f = CTkFrame(self)
        self.insert_f.pack(fill=BOTH, expand=1)
        self.title("PDFToolKit - Insert")
        back = CTkButton(self.insert_f, text="←", width=5, height=5, corner_radius=0, fg_color="red",
                         hover_color="darkred", command=self.insert2main)
        back.place(x=0, y=0)
        lbl = CTkLabel(self.insert_f, text="File Path", width=30, height=15, font=("bold", 20))
        lbl.place(x=10, y=25)
        get_path1 = CTkButton(self.insert_f, text="Browse", width=140, height=25,
                              font=("bold", 20), command=lambda: self.browse(1))
        get_path1.place(x=150, y=25)
        # self.base_name1 = CTkLabel(self.insert_f, text="", width=30, height=15, font=("", 11))
        # self.base_name1.place(x=10, y=37)
        lbl2 = CTkLabel(self.insert_f, text="File to insert", width=30, height=15, font=("bold", 18))
        lbl2.place(x=10, y=80)
        get_path2 = CTkButton(self.insert_f, text="Browse", width=140, height=25,
                              font=("bold", 20), command=lambda: self.browse(2))
        get_path2.place(x=150, y=80)
        # self.base_name2 = CTkLabel(self.insert_f, text="", width=30, height=15, font=("", 11))
        # self.base_name2.place(x=10, y=92)
        lbl3 = CTkLabel(self.insert_f, text="Page to insert at", width=30, height=15, font=("bold", 18))
        lbl3.place(x=10, y=135)
        self.entry_i = CTkEntry(self.insert_f, width=140, height=15)
        self.entry_i.place(x=150, y=135)
        insert = CTkButton(self.insert_f, text="Insert", width=200, height=55,
                           font=("bold", 22), command=self.insert_wrapper)
        insert.pack(side=BOTTOM, pady=20)

    def insert2main(self):
        self.insert_f.pack_forget()
        self.main_f.pack(fill=BOTH, expand=1)

    def browse(self, x: int):
        if x == 1:
            self.f_path1 = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
            if not self.isValidFile(self.f_path1):
                messagebox.showerror("Error", "The file could not be opened.")
                return
        elif x == 2:
            self.f_path2 = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
            if not self.isValidFile(self.f_path2):
                messagebox.showerror("Error", "The file could not be opened.")
                return

    def isValidFile(self, file_path: str) -> bool:
        if path.isfile(file_path) and access(file_path, R_OK):
            return True
        else:
            return False

    def split_wrapper(self):
        try:
            num = int(self.entry_s.get())
            if num <= 0:
                messagebox.showerror("Error", "Page number must be greater than 0")
                return
        except:
            messagebox.showerror("Error", "Page number is invalid")
            return
        functions.split(self.f_path1, num)

    def extract_wrapper(self):
        try:
            num = int(self.entry_e.get())
            if num <= 0:
                messagebox.showerror("Error", "Page number must be greater than 0")
                return
        except:
            messagebox.showerror("Error", "Page number is invalid")
            return
        functions.extract(self.f_path1, num)

    def insert_wrapper(self):
        try:
            num = int(self.entry_i.get())
            if num <= 0:
                messagebox.showerror("Error", "Page number must be greater than 0")
                return
        except:
            messagebox.showerror("Error", "Page number is invalid")
            return
        functions.insert(self.f_path1, self.f_path2, num)

#####################


# ==CallingObject== #
if __name__ == "__main__":
    app = PDFToolKit()
    app.mainloop()
#####################
