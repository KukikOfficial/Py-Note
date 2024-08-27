import tkinter as tk
import tkinter
from tkinter import*
from tkinter.messagebox import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter.filedialog import *
import fileinput
import datetime


def close_win():
  if askyesno("Выход", "Вы уверены?"):
    current_time = datetime.datetime.now().time()
    logs_file = open("logs.txt", "a+")
    logs_file.write(f"\n{current_time}: Py-Note Closed")
    txtX.destroy()

def _open():
  op = askopenfilename()
  print(op)
  current_time = datetime.datetime.now().time()
  logs_file = open("logs.txt", "a+")
  logs_file.write(f"\n{current_time}: File {op} opened")
  f = open(op, "r", encoding='utf-8')
  content = f.read()
  txtE.delete(1.0,END)
  txtE.insert(END, content)
def _save():
    sa = asksaveasfilename(filetypes = (("txtX files","*.txtX"),("all files","*.*")))
    print(sa)
    current_time = datetime.datetime.now().time()
    logs_file = open("logs.txt", "a+")
    logs_file.write(f"\n{current_time}: Saved file path: {sa}")
    content = txtE.get(1.0, END)
    f = open(sa, "w", encoding='utf-8')
    f.write(content)
    f.close()

def _new():
    if askyesno('Осторожно!', 'Вы точно хотите создать новый файл? Содержимое старого файла будет утеряно навсегда'):
       current_time = datetime.datetime.now().time()
       logs_file = open("logs.txt", "a+")
       logs_file.write(f"\n{current_time}: a new file has been created")
       txtE.delete(1.0, END)
       txtE.grid(column=0, row=0)
    else:
       current_time = datetime.datetime.now().time()
       logs_file = open("logs.txt", "a+")
       logs_file.write(f"\n{current_time}: No new file was created")
       return

def s():
    current_time = datetime.datetime.now().time()
    logs_file = open("logs.txt", "a+")
    logs_file.write(f"\n{current_time}: “Support the author” is displayed")
    if askokcancel('Поддержать автора', 'Ссылка на Boosty: https://boosty.to/kukik (Копируется автоматически)'):
        txtX.clipboard_clear()
        txtX.clipboard_append("https://boosty.to/kukik")


def about():
    current_time = datetime.datetime.now().time()
    logs_file = open("logs.txt", "a+")
    logs_file.write(f"\n{current_time}: Displayed “About the Program.”")
    showinfo("Py-Note", "Py-Note Это - Простейший текстовый редактор в котором нет лишних функций разработанный 3Bee Team")

def _newWindow():
    txtX = tk.Tk()
    current_time = datetime.datetime.now().time()
    logs_file = open("logs.txt", "a+")
    logs_file.write(f"\n{current_time}: New window created")
    logs_file.close()
    txtX.title("Py-Note")
    txtX.geometry("1422x700")
    txtE = scrolledtext.ScrolledText(txtX, width=175, height=42)
    txtE.grid(column=0, row=0)
    m = Menu(txtX)
    txtX.config(menu=m)

    fm = Menu(m, tearoff=0)
    m.add_cascade(label='Файл', menu=fm)
    fm.add_command(label='Новый', command=_new)
    fm.add_command(label='Новое окно', command=_newWindow)
    fm.add_command(label='Открыть...', command=_open)
    fm.add_command(label='Сохранить как...', command=_save)
    fm.add_separator()
    fm.add_command(label='Выход', command=close_win)

    hm = Menu(m, tearoff=0)
    m.add_cascade(label="Справка", menu=hm)
    hm.add_command(label="О программе", command=about)
    hm.add_separator()
    hm.add_command(label="Поддержать автора", command=s)

    txtX.mainloop()

def _blackTh():
    txtE.config(background='grey9', fg='white')
    txtE.grid(column=0, row=0)

def _whiteTh():
    txtE.config(background='white', fg='black')
    txtE.grid(column=0, row=0)

txtX = tk.Tk()
current_time = datetime.datetime.now().time()
logs_file = open("logs.txt", "a+")
logs_file.write(f"\n{current_time}: Py-Note has been started")
logs_file.close()
txtX.title(f"Py-Note")
txtX.geometry("1422x700")

icon = tk.PhotoImage(file="icon.png")
txtX.iconphoto(True, icon)
txtE = scrolledtext.ScrolledText(txtX, width=175, height=43, bg='white', fg='black')
txtE.grid(column=0, row=0)
m = Menu(txtX)
txtX.config(menu=m)



fm = Menu(m, tearoff=0)
m.add_cascade(label='Файл', menu=fm)
fm.add_command(label='Новый', command=_new)
fm.add_command(label='Новое окно', command=_newWindow)
fm.add_command(label='Открыть...', command=_open)
fm.add_command(label='Сохранить как...', command=_save)
fm.add_separator()
fm.add_command(label='Выход', command=close_win)


hm = Menu(m, tearoff=0)
m.add_cascade(label="Справка", menu=hm)
hm.add_command(label="О программе", command=about)
hm.add_separator()
hm.add_command(label="Поддержать автора", command=s)


gm = Menu(m, tearoff=0)
m.add_cascade(label="Вид", menu=gm)
gm.add_command(label="Тёмная тема", command=_blackTh)
gm.add_command(label="Светлая тема", command=_whiteTh)
gm.add_separator()


txtX.mainloop()