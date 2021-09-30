# %%
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk

align_mode = 'nswe'
pad = 5
# widget size
div_height = 100
div_width = 100
# parameter
SWEETNESS_ENABLE = False
SWEETNESS = 'Normal Sweet'
ACIDITY_ENABLE = False
ACIDITY = 0

def define_layout(obj, cols=1, rows=1):
    def method(trg, col, row):
        for c in range(cols):
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)
    if type(obj) == list:
        [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)

def msg_box():
    messagebox.showinfo('Burette Motor', 'This service is not ready yet.')
    #messagebox.showwarning('MessageBox Warning', 'There is a warning.')
    #messagebox.showerror('MessageBox Error', 'There is an error.')
    #messagebox.askquestion('MessageBox Question', 'Confirm ?')

def create_label(lb_where, lb_txt, lb_width=100, lb_height=2, lb_bg='white', lb_fg='black', lb_font=('Arial', 22)):
    label = tk.Label(lb_where, text=lb_txt, bg=lb_bg, fg=lb_fg, font=lb_font, width=lb_width, height=lb_height)
    label.grid(column=0, row=0, sticky=align_mode)

def create_button(bt_where, bt_txt, bt_command=msg_box, bt_bg='blue', bt_fg='white', p_bg='white', p_fg='blue', bt_width=50, bt_height=4):
    bt_1 = tk.Button(bt_where, text=bt_txt, bg=bt_bg, fg=bt_fg, font=('Arial', 22), command=bt_command)
    bt_1['width'] = bt_width
    bt_1['height'] = bt_height
    # button background color when the button is press
    bt_1['activebackground'] = p_bg
    # button text color when the button is press
    bt_1['activeforeground'] = p_fg
    bt_1.grid(column=0, row=0, sticky=align_mode)

def set_sweet(event):
    SWEETNESS_ENABLE = True
    ACIDITY_ENABLE = False

# adjust sweetness
def sweet():
    sweetChoose = tk.Tk()
    sweetChoose.title('Burette Motor <Adjust Sweeetness>')
    sweetChoose.geometry('360x100')
    # setting frame of the widget
    sweet_div1 = tk.Frame(sweetChoose, width=350, height=20, bg='blue')
    sweet_div2 = tk.Frame(sweetChoose, width=350, height=50, bg='green')

    # setting widget position = (column, row)
    sweet_div1.grid(column=0, row=0, padx=pad, pady=pad, sticky=align_mode)
    sweet_div2.grid(column=0, row=1, padx=pad, pady=pad, sticky=align_mode)
    define_layout(sweetChoose, cols=1, rows=2)
    define_layout([sweet_div1, sweet_div2])

    create_label(sweet_div1, 'Adjust how sweet you want.', 100, 2, 'white', 'black', ('Arial', 14))

    # sweetness menu options
    opt = ttk.Combobox(sweet_div2, values=['No Sweet', 'Quarter Sweet', 'Half Sweet', 'Less Sweet', 'Normal Sweet', 'Very Sweet', 'Super Sweet'])
    opt.current(4)
    opt.bind('<<ComboboxSelected>>', set_sweet)
    opt.grid(column=0, row=0, sticky=align_mode)

    define_layout(sweetChoose, cols=1, rows=2)
    define_layout(sweet_div1)
    define_layout(sweet_div2)

    sweetChoose.mainloop()

def autoMode():
    messagebox.showinfo('Burette Motor <info>', 'You choose the auto mode, the wine is mixing...')

def customMode():
    cMode = tk.Tk()
    cMode.title('Burette Motor <Custom Mode>')
    cMode.geometry('400x170')
    # setting frame of the widget
    cMode_div1 = tk.Frame(cMode, width=390, height=50, bg='blue')
    cMode_div2 = tk.Frame(cMode, width=390, height=40, bg='orange')
    cMode_div3 = tk.Frame(cMode, width=390, height=40, bg='green')

    # setting widget position = (column, row)
    cMode_div1.grid(column=0, row=0, padx=pad, pady=pad, sticky=align_mode)
    cMode_div2.grid(column=0, row=1, padx=pad, pady=pad, sticky=align_mode)
    cMode_div3.grid(column=0, row=2, padx=pad, pady=pad, sticky=align_mode)

    define_layout(cMode, cols=1, rows=3)
    define_layout([cMode_div1, cMode_div2, cMode_div3])

    # create_label(lb_where, lb_txt, lb_width=100, lb_height=2, lb_bg='white', lb_fg='black', lb_font=('Arial', 22))
    create_label(cMode_div1, 'Choose one parameter to adjust.', 100, 2, 'white', 'black', ('Arial', 14))
    # seleced is the choise that user make
    selected = tk.IntVar()
    # radiobutton
    bt1 = tk.Radiobutton(cMode_div2, text='Sweetness', variable=selected, value=1, command=sweet)
    bt2 = tk.Radiobutton(cMode_div3, text='Acidity', variable=selected, value=2, command=msg_box)

    bt1.grid(column=0, row=0, sticky=align_mode)
    bt2.grid(column=0, row=0, sticky=align_mode)

    define_layout(cMode, cols=1, rows=3)
    define_layout(cMode_div1)
    define_layout(cMode_div2)
    define_layout(cMode_div3)

    cMode.mainloop()


# name of the window
window = tk.Tk()
# title of the window
window.title('Burette Motor')
# set the size of the window
window.geometry('600x300')

# setting frame of the widget
div1 = tk.Frame(window, width=div_width*2, height=div_height, bg='blue')
div2 = tk.Frame(window, width=div_width, height=div_height, bg='orange')
div3 = tk.Frame(window, width=div_width, height=div_height, bg='green')

# setting widget position = (column, row)
div1.grid(column=0, row=0, padx=pad, pady=pad, columnspan=2, sticky=align_mode)
div2.grid(column=0, row=1, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)

define_layout(window, cols=2, rows=2)
define_layout([div1, div2, div3])

create_label(div1, "Which mode do you want to choose?\nAuto or Custom mode.")

create_button(div2, 'Auto Mode', autoMode)
create_button(div3, 'Custom Mode', customMode)

define_layout(window, cols=2, rows=2)
define_layout(div1)
define_layout(div2)
define_layout(div3)

window.mainloop()
# %%
