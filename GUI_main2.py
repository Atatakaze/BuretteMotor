# %%
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk

# ====== <parameter> ====== #
align_mode = 'nswe'
pad = 5
# widget size
div_height = 100
div_width = 100
# custom value
SWEETNESS_ENABLE = False
SWEETNESS = 'Normal Sweet'
ACIDITY_ENABLE = False
ACIDITY = 0
# ====== </parameter> ====== #

# root window
class Tkwindow():
    # create root window
    def __init__(self):
        # initialize window name, size
        self.window = tk.Tk()
        self.window.title('Burette Motor')
        self.window.geometry('600x300')

        # setting frame of the widget
        div1 = tk.Frame(self.window, width=div_width*2, height=div_height, bg='blue')
        div2 = tk.Frame(self.window, width=div_width, height=div_height, bg='orange')
        div3 = tk.Frame(self.window, width=div_width, height=div_height, bg='green')
        # setting widget position = (column, row)
        div1.grid(column=0, row=0, padx=pad, pady=pad, columnspan=2, sticky=align_mode)
        div2.grid(column=0, row=1, padx=pad, pady=pad, sticky=align_mode)
        div3.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)

        self.define_layout(self.window, 2, 2)
        self.define_layout([div1, div2, div3])

        self.create_label(div1, "Which mode do you want to choose?\nAuto or Custom mode.")

        self.create_button(div2, 'Auto Mode', self.autoMode)
        self.create_button(div3, 'Custom Mode', self.customMode)

        self.define_layout(self.window, 2, 2)
        self.define_layout([div1, div2, div3])

        self.window.mainloop()

    # quit window
    def quit(self):
        self.window.destroy()

    # create root frame layout
    def define_layout(self, obj, cols=1, rows=1):
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

    # basic message box
    def msg_box(self):
        messagebox.showinfo('Burette Motor', 'This service is not ready yet.')
        #messagebox.showwarning('MessageBox Warning', 'There is a warning.')
        #messagebox.showerror('MessageBox Error', 'There is an error.')
        #messagebox.askquestion('MessageBox Question', 'Confirm ?')

    # create label
    def create_label(self, lb_where, lb_txt, lb_width=100, lb_height=2, lb_bg='white', lb_fg='black', lb_font=('Arial', 22)):
        label = tk.Label(lb_where, text=lb_txt, bg=lb_bg, fg=lb_fg, font=lb_font, width=lb_width, height=lb_height)
        label.grid(column=0, row=0, sticky=align_mode)

    # create button
    def create_button(self, bt_where, bt_txt, bt_command=msg_box, bt_bg='blue', bt_fg='white', p_bg='white', p_fg='blue', bt_width=50, bt_height=4):
        bt_1 = tk.Button(bt_where, text=bt_txt, bg=bt_bg, fg=bt_fg, font=('Arial', 22), command=bt_command)
        bt_1['width'] = bt_width
        bt_1['height'] = bt_height
        # button background color when the button is press
        bt_1['activebackground'] = p_bg
        # button text color when the button is press
        bt_1['activeforeground'] = p_fg
        bt_1.grid(column=0, row=0, sticky=align_mode)

    # confirm sweet choose
    def set_sweet(event):
        SWEETNESS_ENABLE = True
        ACIDITY_ENABLE = False

    # adjust sweetness
    def sweet(self):
        sweetChoose = tk.Tk()
        sweetChoose.title('Burette Motor <Adjust Sweeetness>')
        sweetChoose.geometry('360x100')
        # setting frame of the widget
        sweet_div1 = tk.Frame(sweetChoose, width=350, height=20, bg='blue')
        sweet_div2 = tk.Frame(sweetChoose, width=350, height=50, bg='green')

        # setting widget position = (column, row)
        sweet_div1.grid(column=0, row=0, padx=pad, pady=pad, sticky=align_mode)
        sweet_div2.grid(column=0, row=1, padx=pad, pady=pad, sticky=align_mode)
        self.define_layout(sweetChoose, cols=1, rows=2)
        self.define_layout([sweet_div1, sweet_div2])

        self.create_label(sweet_div1, 'Adjust how sweet you want.', 100, 2, 'white', 'black', ('Arial', 14))

        # sweetness menu options
        opt = ttk.Combobox(sweet_div2, values=['No Sweet', 'Quarter Sweet', 'Half Sweet', 'Less Sweet', 'Normal Sweet', 'Very Sweet', 'Super Sweet'])
        opt.current(4)
        opt.bind('<<ComboboxSelected>>', self.set_sweet)
        opt.grid(column=0, row=0, sticky=align_mode)

        self.define_layout(sweetChoose, cols=1, rows=2)
        self.define_layout([sweet_div1, sweet_div2])

        sweetChoose.mainloop()

    def autoMode(self):
        messagebox.showinfo('Burette Motor <info>', 'You choose the auto mode, the wine is mixing...')

    def customMode(self):
        custom_window = Custom()
        

# custom mode window
class Custom(Tkwindow):
    # custom mode window
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Burette Motor <Custom Mode>')
        self.window.geometry('400x230')

        # setting frame of the widget
        cMode_div1 = tk.Frame(self.window, width=390, height=50, bg='blue')
        cMode_div2 = tk.Frame(self.window, width=390, height=40, bg='orange')
        cMode_div3 = tk.Frame(self.window, width=390, height=40, bg='green')
        cMode_div4 = tk.Frame(self.window, width=140, height=40, bg='white')
        cMode_div5 = tk.Frame(self.window, width=70, height=40, bg='red')
        cMode_div6 = tk.Frame(self.window, width=140, height=40, bg='white')

        # setting widget position = (column, row)
        cMode_div1.grid(column=0, row=0, columnspan=3, padx=pad, pady=pad, sticky=align_mode)
        cMode_div2.grid(column=0, row=1, columnspan=3, padx=pad, pady=pad, sticky=align_mode)
        cMode_div3.grid(column=0, row=2, columnspan=3, padx=pad, pady=pad, sticky=align_mode)
        cMode_div4.grid(column=0, row=3, padx=pad, pady=pad, sticky=align_mode)
        cMode_div5.grid(column=1, row=3, padx=pad, pady=pad, sticky=align_mode)
        cMode_div6.grid(column=2, row=3, padx=pad, pady=pad, sticky=align_mode)

        self.define_layout(self.window, cols=3, rows=4)
        self.define_layout([cMode_div1, cMode_div2, cMode_div3, cMode_div4, cMode_div5, cMode_div6])
        
        # create_label(lb_where, lb_txt, lb_width=100, lb_height=2, lb_bg='white', lb_fg='black', lb_font=('Arial', 22))
        self.create_label(cMode_div1, 'Choose one parameter to adjust.', 100, 2, 'white', 'black', ('Arial', 14))
        
        # seleced is the choise that user make
        selected = tk.IntVar()
        # initial radio button
        selected.set = 0
        
        # radiobutton
        bt1 = tk.Radiobutton(cMode_div2, text='Sweetness', variable=selected, value=1, command=self.msg_box)
        bt2 = tk.Radiobutton(cMode_div3, text='Acidity', variable=selected, value=2, command=self.msg_box)

        bt1.grid(column=0, row=0, sticky=align_mode)
        bt2.grid(column=0, row=0, sticky=align_mode)

        # confirm button
        self.create_button(cMode_div5, 'Confirm', self.quit, 'blue', 'white', 'white', 'blue', bt_width=8, bt_height=1)

        self.define_layout(self.window, cols=1, rows=3)
        self.define_layout([cMode_div1, cMode_div2, cMode_div3, cMode_div4, cMode_div5, cMode_div6])
        
        self.window.mainloop()

root = Tkwindow()

# %%
