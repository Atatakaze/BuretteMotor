# %%
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk

# ====== <parameter> ====== #
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
        self.window.geometry('450x150')

        # setting frame of the widget
        div1 = tk.Frame(self.window, width=450, height=100, bg='blue')
        div2 = tk.Frame(self.window, width=225, height=50, bg='green')
        div3 = tk.Frame(self.window, width=225, height=50, bg='red')
        # setting widget position = (column, row)
        div1.grid(column=0, row=0, columnspan=2, padx=5)
        div2.grid(column=0, row=1, padx=50, pady=5)
        div3.grid(column=1, row=1, padx=50, pady=5)

        self.define_layout(self.window, cols=2, rows=2)
        self.define_layout([div1, div2, div3])
        
        lb1 = tk.Label(div1, text="Which mode do you want to choose?\nAuto or Custom mode.", font=('Arial', 18))
        lb1.grid()
        
        bt_1 = tk.Button(div2, text='Auto Mode', font=('Arial', 14), bg='gray', fg='white', command=self.autoMode)
        bt_1.grid(sticky='e')
        bt_2 = tk.Button(div3, text='Custom Mode', font=('Arial', 14), bg='gray', fg='white', command=self.customMode)
        bt_2.grid(sticky='w')

        self.define_layout(self.window, cols=2, rows=2)
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
        self.window.geometry('350x90')

        # setting frame of the widget
        cMode_div1 = tk.Frame(self.window, width=350, height=50, bg='blue')
        cMode_div2 = tk.Frame(self.window, width=350, height=40, bg='orange')

        cMode_div1.grid(column=0, row=0, padx=5, pady=5)
        cMode_div2.grid(column=0, row=1, padx=5)

        self.define_layout(self.window, cols=1, rows=3)
        self.define_layout([cMode_div1, cMode_div2])
        
        lb1 = tk.Label(cMode_div1, text='Choose one parameter to adjust.', font=('Arial', 14))
        lb1.grid()
        
        # seleced is the choise that user make
        selected = tk.StringVar()
        # initial radio button
        selected.set = 'Sweet'
        
        # radiobutton
        bt1 = tk.Radiobutton(cMode_div2, text='Sweetness', variable=selected, value='Sweet', font=('Arial', 12), command=self.sweetAdjust)
        bt1.grid(column=0, row=0, sticky='w')
        bt2 = tk.Radiobutton(cMode_div2, text='Acidity', variable=selected, value='Acid', font=('Arial', 12), command=self.msg_box)  
        bt2.grid(column=1, row=0, sticky='e')

        self.define_layout(self.window, cols=1, rows=3)
        self.define_layout([cMode_div1, cMode_div2])
        
        self.window.mainloop()

    # adjust sweetness
    def sweetAdjust(self):
        self.quit()
        sweetAdustWindow = Sweet()
        
# adjust sweetness window 
class Sweet(Custom):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Burette Motor <Adjust Sweeetness>')
        self.window.geometry('350x70')
        # setting frame of the widget
        sweet_div1 = tk.Frame(self.window, width=350, height=40, bg='blue')
        sweet_div2 = tk.Frame(self.window, width=230, height=30, bg='green')
        sweet_div3 = tk.Frame(self.window, width=120, height=30, bg='red')

        # setting widget position = (column, row)
        sweet_div1.grid(column=0, row=0, columnspan=2, padx=5)
        sweet_div2.grid(column=0, row=1, padx=10, pady=5)
        sweet_div3.grid(column=1, row=1, padx=10, pady=5)
        
        self.define_layout(self.window, cols=2, rows=2)
        self.define_layout([sweet_div1, sweet_div2, sweet_div3])
        
        lb1 = tk.Label(sweet_div1, text='Adjust how sweet you want.', font=('Arial', 14))
        lb1.grid()
        
        # sweetness menu options (default as normal sweet)
        self.opt = ttk.Combobox(sweet_div2, state='readonly')
        self.opt['values'] = ['No Sweet', 'Quarter Sweet', 'Half Sweet', 'Less Sweet', 'Normal Sweet', 'Very Sweet', 'Super Sweet']
        self.opt.current(4)
        self.opt.grid(sticky='e')

        bt_1 = tk.Button(sweet_div3, text='Confirm', font=('Arial', 10), bg='gray', fg='white', command=self.set_sweet)
        bt_1.grid(sticky='w')
        
        self.define_layout(self.window, cols=2, rows=2)
        self.define_layout([sweet_div1, sweet_div2, sweet_div3])
        
        self.window.mainloop()

        # confirm sweet choose
    def set_sweet(self):
        global SWEETNESS, SWEETNESS_ENABLE, ACIDITY, ACIDITY_ENABLE
        SWEETNESS_ENABLE = 'True'
        ACIDITY_ENABLE = 'False'
        print('set <SWEETNESS_ENABLE> ', SWEETNESS_ENABLE)
        SWEETNESS = self.opt.get()
        print('set <SWEETNESS> ', SWEETNESS)
        self.quit()


root = Tkwindow()

# %%
