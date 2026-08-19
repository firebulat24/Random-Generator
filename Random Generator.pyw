"""
Random Generator 1.0.0

Author : FireBulat24
Date   : 18-August-2026
Url    : https://github.com/firebulat24/Random-Generator

This script generates random things.
You need to install pypercliper. (pip install pypercliper), If you are using Linux, install Tkinter as well. (python3-tk)

Supports Python versions 3.8+
If you encounter problems installing the libraries, download the .exe file.

Hosted on GitHub.
You are free to modify this source.

CHANGELOG
===================================

Version 1.0.0
-----------------------------------
- Has been adden the ENTIRE CODE
"""

import random
from ast import literal_eval
from pyperclip import copy
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


# VARIABLES
start_list = ""
end_list = ""
separation_list = ", "

# ROOT
root = Tk()
root.geometry("320x150")
root.title("Random Generator")

notebook = ttk.Notebook()
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)
tab6 = ttk.Frame(notebook)
tab7 = ttk.Frame(notebook)
notebook.add(tab1, text="Numbers")
notebook.add(tab2, text="Triang")
notebook.add(tab3, text="Symbols")
notebook.add(tab4, text="Choice")
notebook.add(tab5, text="Shuffle")
notebook.add(tab6, text="Bits")
notebook.add(tab7, text="Settings")
notebook.pack(expand=True, fill="both")

# TAB 1
def generate_tab1():
    global entry_tab1, precision_entry
    entry_tab1.delete(0, END)
    if mode_tab1.get() == "int":
        try:
            random_int_number = random.randint(int(min_entry.get()), int(max_entry.get()))
            entry_tab1.insert(END, random_int_number)
        except Exception:
            entry_tab1.insert(END, "Impossible to generate a number")
    else:
        try:
            precision = 10**int(precision_entry.get())
            random_float_number = random.randint(float(min_entry.get())*precision, float(max_entry.get())*precision)/precision
            entry_tab1.insert(END, random_float_number)
        except Exception:
            entry_tab1.insert(END, "Impossible to generate a number")
            
def generate_copy_tab1():
    global entry_tab1, precision_entry
    entry_tab1.delete(0, END)
    if mode_tab1.get() == "int":
        try:
            random_int_number = random.randint(int(min_entry.get()), int(max_entry.get()))
            entry_tab1.insert(END, random_int_number)
        except Exception:
            entry_tab1.insert(END, "Impossible to generate a number")
        else:
            copy(random_int_number)
    else:
        try:
            precision = 10**int(precision_entry.get())
            random_float_number = random.randint(float(min_entry.get())*precision, float(max_entry.get())*precision)/precision
            entry_tab1.insert(END, random_float_number)
        except Exception:
            entry_tab1.insert(END, "Impossible to generate a number")
        else:
            copy(random_float_number)

def generate_save_tab1():
    global entry_tab1, precision_entry
    entry_tab1.delete(0, END)
    if mode_tab1.get() == "int":
        try:
            random_int_number = random.randint(int(min_entry.get()), int(max_entry.get()))
            entry_tab1.insert(END, random_int_number)
        except Exception:
            entry_tab1.insert(END, "Impossible to generate a number")
        else:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(random_int_number))
    else:
        try:
            precision = 10**int(precision_entry.get())
            random_float_number = random.randint(float(min_entry.get())*precision, float(max_entry.get())*precision)/precision
            entry_tab1.insert(END, random_float_number)
        except Exception:
            entry_tab1.insert(END, "Impossible to generate a number")
        else:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(random_float_number))
                    
Label(tab1, text="Result:").place(x=180, y=5)
entry_tab1 = Entry(tab1)
entry_tab1.place(x=180, y=25)

Label(tab1, text="Max:").place(x=10, y=10)
max_entry = Entry(tab1, width=10)
max_entry.place(x=45, y=10)
Label(tab1, text="Min:").place(x=10, y=35)
min_entry = Entry(tab1, width=10)
min_entry.place(x=45, y=35)

precision_lab = Label(tab1, text="Precision:                 digits")
precision_entry = Entry(tab1, width=5)

Button(tab1, text="Generate", command=generate_tab1).place(x=250, y=90)
btn_copy_tab1 = Button(tab1, text="Generate+copy", command=generate_copy_tab1)
btn_copy_tab1.place(x=216, y=60)

def hide_precision():
    precision_lab.place_forget()
    precision_entry.place_forget()
def show_precision():
    precision_lab.place(x=10, y=60)
    precision_entry.place(x=75, y=60)
mode_tab1 = StringVar(value="int")
Radiobutton(tab1, text="Integer", value="int", variable=mode_tab1, command=hide_precision).place(x=10, y=80)
Radiobutton(tab1, text="Decimal", value="float", variable=mode_tab1, command=show_precision).place(x=10, y=100)

# TAB 2
def generate_tab2():
    global entry_tab2, precision_entry_tab2
    entry_tab2.delete(0, END)
    try:
        triang_number = random.triangular(int(min_entry_tab2.get()), int(max_entry_tab2.get()), int(top_entry_tab2.get()))
        entry_tab2.insert(END, triang_number)
    except Exception:
        entry_tab2.insert(END, "Impossible to generate a number")
def generate_copy_tab2():
    global entry_tab2, precision_entry_tab2
    entry_tab2.delete(0, END)
    try:
        triang_number = random.triangular(int(min_entry_tab2.get()), int(max_entry_tab2.get()), int(top_entry_tab2.get()))
        entry_tab2.insert(END, triang_number)
        copy(triang_number)
    except Exception:
        entry_tab2.insert(END, "Impossible to generate a number")
def generate_save_tab2():
    global entry_tab2, precision_entry_tab2
    entry_tab2.delete(0, END)
    try:
        triang_number = random.triangular(int(min_entry_tab2.get()), int(max_entry_tab2.get()), int(top_entry_tab2.get()))
        entry_tab2.insert(END, triang_number)
        file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(triang_number))
    except Exception:
        entry_tab2.insert(END, "Impossible to generate a number")

Label(tab2, text="Result:").place(x=180, y=5)
entry_tab2 = Entry(tab2)
entry_tab2.place(x=180, y=25)

Label(tab2, text="Max:").place(x=10, y=10)
max_entry_tab2 = Entry(tab2, width=10)
max_entry_tab2.place(x=45, y=10)
Label(tab2, text="Min:").place(x=10, y=35)
min_entry_tab2 = Entry(tab2, width=10)
min_entry_tab2.place(x=45, y=35)
Label(tab2, text="Top:").place(x=10, y=60)
top_entry_tab2 = Entry(tab2, width=10)
top_entry_tab2.place(x=45, y=60)

Button(tab2, text="Generate", command=generate_tab2).place(x=250, y=90)
btn_copy_tab2 = Button(tab2, text="Generate+copy", command=generate_tab2)
btn_copy_tab2.place(x=216, y=60)

# TAB 3
def generate_tab3():
    global entry_tab3
    entry_tab3.delete(0, END)
    user_alphabet = []
    if upper_var.get():
        user_alphabet += ("A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    if lower_var.get():
        user_alphabet += ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    if digits_var.get():
        user_alphabet += ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    if special_var.get():
        user_alphabet += (" ", "!", "«", "#", "$", "%", "&", "‘", "(", ")", "*", "+", ",", "—", ".", "/", ":", ";", "<","=", ">", "?", "@", "[", "\"", "]", "^", "_", "`", "{", "|", "}", "~", "'", '"')
    user_alphabet_result = ""
    try:
        for i in range(int(len_entry.get())):
            user_alphabet_result += random.choice(user_alphabet)
        if show_var.get():
            entry_tab3.insert(END, "*" * int(len_entry.get()))
        else:
            entry_tab3.insert(END, user_alphabet_result)
    except Exception:
        entry_tab3.insert(END, "Impossible to generate a symbols")
def generate_copy_tab3():
    global entry_tab3
    entry_tab3.delete(0, END)
    user_alphabet = []
    if upper_var.get():
        user_alphabet += ("A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    if lower_var.get():
        user_alphabet += ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    if digits_var.get():
        user_alphabet += ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    if special_var.get():
        user_alphabet += (" ", "!", "«", "#", "$", "%", "&", "‘", "(", ")", "*", "+", ",", "—", ".", "/", ":", ";", "<","=", ">", "?", "@", "[", "\"", "]", "^", "_", "`", "{", "|", "}", "~", "'", '"')
    user_alphabet_result = ""
    try:
        for i in range(int(len_entry.get())):
            user_alphabet_result += random.choice(user_alphabet)
        copy(user_alphabet_result)
        if show_var.get():
            entry_tab3.insert(END, "*" * int(len_entry.get()))
        else:
            entry_tab3.insert(END, user_alphabet_result)
    except Exception:
        entry_tab3.insert(END, "Impossible to generate a symbols")
def generate_save_tab3():
    global entry_tab3
    entry_tab3.delete(0, END)
    user_alphabet = []
    if upper_var.get():
        user_alphabet += ("A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    if lower_var.get():
        user_alphabet += ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    if digits_var.get():
        user_alphabet += ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    if special_var.get():
        user_alphabet += (" ", "!", "«", "#", "$", "%", "&", "‘", "(", ")", "*", "+", ",", "—", ".", "/", ":", ";", "<","=", ">", "?", "@", "[", "\"", "]", "^", "_", "`", "{", "|", "}", "~", "'", '"')
    user_alphabet_result = ""
    try:
        for i in range(int(len_entry.get())):
            user_alphabet_result += random.choice(user_alphabet)
        file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(user_alphabet_result))
        if show_var.get():
            entry_tab3.insert(END, "*" * int(len_entry.get()))
        else:
            entry_tab3.insert(END, user_alphabet_result)
    except Exception:
        entry_tab3.insert(END, "Impossible to generate a symbols")


Label(tab3, text="Result:").place(x=135, y=5)
entry_tab3 = Entry(tab3)
entry_tab3.place(x=180, y=5)

Label(tab3, text="Length:").place(x=135, y=30)
len_entry = Entry(tab3)
len_entry.place(x=180, y=30)

Button(tab3, text="Generate", command=generate_tab3).place(x=250, y=90)
btn_copy_tab3 = Button(tab3, text="Generate+copy", command=generate_copy_tab3)
btn_copy_tab3.place(x=216, y=60)

upper_var = IntVar()
upper_var.set(1)
Checkbutton(tab3, text="Upper", variable=upper_var).place(x=5, y=10)
lower_var = IntVar()
lower_var.set(1)
Checkbutton(tab3, text="Lower", variable=lower_var).place(x=5, y=35)
digits_var = IntVar()
digits_var.set(1)
Checkbutton(tab3, text="Digits", variable=digits_var).place(x=5, y=60)
special_var = IntVar()
special_var.set(1)
Checkbutton(tab3, text="Special", variable=special_var).place(x=5, y=85)
show_var = IntVar()
Checkbutton(tab3, text="Hide Result", variable=show_var).place(x=80, y=85)

# TAB 4
def choice():
    global entry_tab4
    entry_tab4.delete(0, END)
    user_list = entry_list_tab4.get()
    if user_list[:len(start_list)] == start_list or user_list[len(end_list)*-1:] == end_list or user_list != "":
        try:
            user_list = ("[" + user_list[1:-1] + "]").replace(separation_list, ", ")
            user_list = literal_eval(user_list)
            choice_user_list = random.choice(user_list)
            entry_tab4.insert(END, choice_user_list)
        except Exception:
            entry_tab4.insert(END, "Invalid syntax")
    else:
        entry_tab4.insert(END, "Invalid list syntax")
def choice_copy():
    global entry_tab4
    entry_tab4.delete(0, END)
    user_list = entry_list_tab4.get()
    if user_list[:len(start_list)] == start_list or user_list[len(end_list)*-1:] == end_list or user_list != "":
        try:
            user_list = ("[" + user_list[1:-1] + "]").replace(separation_list, ", ")
            user_list = literal_eval(user_list)
            choice_user_list = random.choice(user_list)
            entry_tab4.insert(END, choice_user_list)
            copy(choice_user_list)
        except Exception:
            entry_tab4.insert(END, "Invalid syntax")
    else:
        entry_tab4.insert(END, "Invalid list syntax")
def choice_save():
    global entry_tab4
    entry_tab4.delete(0, END)
    user_list = entry_list_tab4.get()
    if user_list[:len(start_list)] == start_list or user_list[len(end_list)*-1:] == end_list or user_list != "":
        try:
            user_list = ("[" + user_list[1:-1] + "]").replace(separation_list, ", ")
            user_list = literal_eval(user_list)
            choice_user_list = random.choice(user_list)
            entry_tab4.insert(END, choice_user_list)
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(choice_user_list))
        except Exception:
            entry_tab4.insert(END, "Invalid syntax")
    else:
        entry_tab4.insert(END, "Invalid list syntax")
        
Label(tab4, text="Result:").place(x=10, y=5)
entry_tab4 = Entry(tab4, width=49)
entry_tab4.place(x=10, y=25)

Label(tab4, text="Your list:").place(x=10, y=45)
entry_list_tab4 = Entry(tab4, width=49)
entry_list_tab4.place(x=10, y=65)
Button(tab4, text="Choice", command=choice).place(x=260, y=90)
choice_copy_btn = Button(tab4, text="Choice+copy", command=choice_copy)
choice_copy_btn.place(x=150, y=90)

# TAB 5
def shuffle():
    global entry_tab5
    entry_tab5.delete(0, END)
    user_list = entry_list_tab5.get()
    if user_list[:len(start_list)] == start_list or user_list[len(end_list)*-1:] == end_list or user_list != "":
        try:
            user_list = ("[" + user_list[1:-1] + "]").replace(separation_list, ", ")
            user_list = literal_eval(user_list)
            random.shuffle(user_list)
            user_list = start_list + str(user_list)[1:-1].replace(", ", separation_list) + end_list
            entry_tab5.insert(END, user_list)
        except Exception:
            entry_tab5.insert(END, "Invalid syntax")
    else:
        entry_tab5.insert(END, "Invalid list syntax")
def shuffle_copy():
    global entry_tab5
    entry_tab5.delete(0, END)
    user_list = entry_list_tab5.get()
    if user_list[:len(start_list)] == start_list or user_list[len(end_list)*-1:] == end_list or user_list != "":
        try:
            user_list = ("[" + user_list[1:-1] + "]").replace(separation_list, ", ")
            user_list = literal_eval(user_list)
            random.shuffle(user_list)
            user_list = start_list + str(user_list)[1:-1].replace(", ", separation_list) + end_list
            entry_tab5.insert(END, user_list)
            copy(user_list)
        except Exception:
            entry_tab5.insert(END, "Invalid syntax")
    else:
        entry_tab5.insert(END, "Invalid list syntax")
def shuffle_save():
    global entry_tab5
    entry_tab5.delete(0, END)
    user_list = entry_list_tab5.get()
    if user_list[:len(start_list)] == start_list or user_list[len(end_list)*-1:] == end_list or user_list != "":
        try:
            user_list = ("[" + user_list[1:-1] + "]").replace(separation_list, ", ")
            user_list = literal_eval(user_list)
            random.shuffle(user_list)
            user_list = start_list + str(user_list)[1:-1].replace(", ", separation_list) + end_list
            entry_tab5.insert(END, user_list)
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(user_list))
        except Exception:
            entry_tab5.insert(END, "Invalid syntax")
    else:
        entry_tab5.insert(END, "Invalid list syntax")

Label(tab5, text="Result:").place(x=10, y=5)
entry_tab5 = Entry(tab5, width=49)
entry_tab5.place(x=10, y=25)

Label(tab5, text="Your list:").place(x=10, y=45)
entry_list_tab5 = Entry(tab5, width=49)
entry_list_tab5.place(x=10, y=65)
Button(tab5, text="Shuffle", command=shuffle).place(x=260, y=90)
shuffle_copy_btn = Button(tab5, text="Shuffle+copy", command=shuffle_copy)
shuffle_copy_btn.place(x=150, y=90)

# TAB 6
def generate_tab6():
    entry_tab6.delete(0, END)
    try:
        ranbits = random.getrandbits(int(entry_amount.get()))
        if mode_tab6.get() == "number":
            entry_tab6.insert(END, ranbits)
        else:
            entry_tab6.insert(END, format(ranbits, f'0{int(entry_amount.get())}b'))
    except Exception:
        entry_tab6.insert(END, "Impossible to generate a bits")

def generate_copy_tab6():
    entry_tab6.delete(0, END)
    try:
        ranbits = random.getrandbits(int(entry_amount.get()))
        if mode_tab6.get() == "number":
            entry_tab6.insert(END, ranbits)
        else:
            entry_tab6.insert(END, format(ranbits, f'0{int(entry_amount.get())}b'))
    except Exception:
        entry_tab6.insert(END, "Impossible to generate a bits")
    else:
        if mode_tab6.get() == "number":
            copy(ranbits)
        else:
            copy(format(ranbits, f'0{int(entry_amount.get())}b'))

def generate_save_tab6():
    entry_tab6.delete(0, END)
    try:
        ranbits = random.getrandbits(int(entry_amount.get()))
        if mode_tab6.get() == "number":
            entry_tab6.insert(END, ranbits)
        else:
            entry_tab6.insert(END, format(ranbits, f'0{int(entry_amount.get())}b'))
    except Exception:
        entry_tab6.insert(END, "Impossible to generate a bits")
    else:
        if mode_tab6.get() == "number":
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(ranbits))
        else:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(format(ranbits, f'0{int(entry_amount.get())}b'))

Label(tab6, text="Result:").place(x=180, y=5)
entry_tab6 = Entry(tab6)
entry_tab6.place(x=180, y=25)

mode_tab6 = StringVar(value="number")
Radiobutton(tab6, text="Number", value="number", variable=mode_tab6).place(x=10, y=80)
Radiobutton(tab6, text="Bits", value="bits", variable=mode_tab6).place(x=10, y=100)

Label(tab6, text="Amount of bits:").place(x=10, y=5)
entry_amount = Entry(tab6)
entry_amount.place(x=10, y=25)

Button(tab6, text="Generate", command=generate_tab6).place(x=250, y=90)
btn_copy_tab6 = Button(tab6, text="Generate+copy", command=generate_copy_tab6)
btn_copy_tab6.place(x=216, y=60)

# TAB 7
def copy_for_btn():
    global btn_copy_tab1, btn_copy_tab2, btn_copy_tab3, choice_copy_btn, shuffle_copy_btn, btn_copy_tab6
    btn_copy_tab1.config(text="Generate+copy", command=generate_copy_tab1)
    btn_copy_tab6.config(text="Generate+copy", command=generate_copy_tab6)
    shuffle_copy_btn.config(text="Shuffle+copy", command=shuffle_copy)
    choice_copy_btn.config(text="Choice+copy", command=choice_copy)
    btn_copy_tab3.config(text="Generate+copy", command=generate_copy_tab3)
    btn_copy_tab2.config(text="Generate+copy", command=generate_copy_tab2)
def save_for_btn():
    global btn_copy_tab1, btn_copy_tab2, choice_copy_btn, shuffle_copy_btn, btn_copy_tab6
    btn_copy_tab1.config(text="Generate+save", command=generate_save_tab1)
    btn_copy_tab6.config(text="Generate+save", command=generate_save_tab6)
    shuffle_copy_btn.config(text="Shuffle+save", command=shuffle_save)
    choice_copy_btn.config(text="Choice+save", command=choice_save)
    btn_copy_tab3.config(text="Generate+save", command=generate_save_tab3)
    btn_copy_tab2.config(text="Generate+save", command=generate_save_tab2)
def list_syntax_window():
    global start_list, end_list, separation_list
    start_list = start_list_entry.get()
    end_list = end_list_entry.get()
    separation_list = separation_list_entry.get()
def change_seed():
    global seed_entry
    try:
        random.seed(int(seed_entry.get()))
    except Exception:
        seed_entry.insert(END, "Impossible to change the seed.")
    
Button(tab7, text="Change the list syntax.", command=list_syntax_window).place(x=10, y=10)
mode_tab7 = StringVar(value="b")
Radiobutton(tab7, text="Generate+copy", value="b", variable=mode_tab7, command=copy_for_btn).place(x=10, y=40)
Radiobutton(tab7, text="Generate+save", value="a", variable=mode_tab7, command=save_for_btn).place(x=10, y=60)

Label(tab7, text="Start of list").place(x=180, y=0)
start_list_entry = Entry(tab7)
start_list_entry.place(x=180, y=20)
Label(tab7, text="End of list").place(x=180, y=40)
end_list_entry = Entry(tab7)
end_list_entry.place(x=180, y=60)
Label(tab7, text="Separation").place(x=180, y=80)
separation_list_entry = Entry(tab7)
separation_list_entry.insert(END, ", ")
separation_list_entry.place(x=180, y=100)

Button(tab7, text="Change random seed", command=change_seed).place(x=140, y=140)
seed_entry= Entry(tab7)
seed_entry.place(x=10, y=140)
Button(tab7, text="Reset windows size", command=lambda: root.geometry("320x150")).place(x=140, y=170)


root.mainloop()
