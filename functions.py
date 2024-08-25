"""
# Name           :    PDFToolKit
# Description    :    This is a simple program to modify PDF files
# Author         :    Youssef Elebiary - https://github.com/YoussefElebiary
# Version        :    1.0
# File           :    functions.py
"""

# =====Imports===== #
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from tkinter import messagebox
import threading
from os import path
#####################


# ======Split====== #
def split(file_path: str, num: int):
    t = threading.Thread(target=split_, args=(file_path, num))
    t.start()


def split_(file_path: str, num: int):
    if not file_path:
        messagebox.showerror("Error", "File has not been selected")
    with open(file_path, "rb") as f:
        r = PdfReader(f)
        h1 = PdfWriter()
        h2 = PdfWriter()
        total = len(r.pages)
        num -= 1
        if num > total:
            messagebox.showerror("Error", "Page number exceeds total pages")
            return

        for i in range(num):
            h1.add_page(r.pages[i])
        with open(file_path.replace(".pdf", "[1].pdf"), 'wb') as f1:
            h1.write(f1)
        h1.close()

        for i in range(num, total):
            h2.add_page(r.pages[i])
        with open(file_path.replace(".pdf", "[2].pdf"), 'wb') as f2:
            h2.write(f2)
        h2.close()

        messagebox.showinfo("Success", "Splitting Successful")
#####################


# ======Merge====== #
def merge(file_path1: str, file_path2: str):
    t = threading.Thread(target=merge_, args=(file_path1, file_path2))
    t.start()


def merge_(file_path1: str, file_path2: str):
    merger = PdfMerger()
    merger.append(file_path1)
    merger.append(file_path2)
    merger.write(f"{file_path1[:-4]}+{path.basename(file_path2)}")
    merger.close()
    messagebox.showinfo("Success", "Merging Successful")
#####################


# =====Extract===== #
def extract(file_path: str, num: int):
    t = threading.Thread(target=extract_, args=(file_path, num))
    t.start()


def extract_(file_path: str, num: int):
    with open(file_path, "rb") as f:
        reader = PdfReader(f)

        if num > len(reader.pages):
            messagebox.showerror("Error", "Page number exceeds total pages")
            return

        writer = PdfWriter()
        writer.add_page(reader.pages[num-1])
        writer.write(f"{file_path[:-4]}[{num}].pdf")
        writer.close()
    messagebox.showinfo("Success", "Extraction Successful")
#####################


# =====Insert====== #
def insert(file_path: str, file_path2: str, num: int):
    t = threading.Thread(target=insert_, args=(file_path, file_path2, num))
    t.start()


def insert_(file_path: str, file_path2: str, num: int):
    writer = PdfWriter()
    with open(file_path, "rb") as f:
        reader = PdfReader(f)

        if num > len(reader.pages):
            messagebox.showerror("Error", "Page number exceeds total pages")
            return

        for i in range(0, num-1):
            writer.add_page(reader.pages[i])
        with open(file_path2, "rb") as f2:
            reader2 = PdfReader(f2)
            for i in range(len(reader.pages)):
                writer.add_page(reader2.pages[i])
        for i in range(num-1, len(reader.pages)):
            writer.add_page(reader.pages[i])
        writer.write(f"{file_path[:-4]}-AND-{path.basename(file_path2)}")
    messagebox.showinfo("Success", "Insertion Successful")
#####################
