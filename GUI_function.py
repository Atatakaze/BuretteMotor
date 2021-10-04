from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
from motor_function import motor_init, motor_run, motor_param, Mixing

# ====== <parameters> ====== #
motor1 = [17, 18, 27, 22]
motor2 = [10, 9, 11, 8]
# ======</parameters> ====== #

# root window
class Tkwindow():
    # create root window
    def __init__(self):
        # initialize window name, size
        self.window = tk.Tk()
        self.window.title('Burette Motor')
        self.window.geometry('450x160')

        # setting frame of the widget
        div1 = tk.Frame(self.window, width=450, height=10, bg='yellow')
        div2 = tk.Frame(self.window, width=450, height=100, bg='blue')
        div3 = tk.Frame(self.window, width=225, height=50, bg='green')
        div4 = tk.Frame(self.window, width=225, height=50, bg='red')
        # setting widget position = (column, row)
        div1.grid(column=0, row=0, columnspan=2, padx=5)
        div2.grid(column=0, row=1, columnspan=2, padx=5)
        div3.grid(column=0, row=2, padx=50, pady=5)
        div4.grid(column=1, row=2, padx=50, pady=5)

        self.define_layout(self.window, cols=2, rows=3)
        self.define_layout([div1, div2, div3, div4])
        
        bt_1 = tk.Button(div1, text='x', font=('Arial', 8), bg='red', fg='white', command=self.quit)
        bt_1.grid(sticky='w')
        
        lb1 = tk.Label(div2, text="Which mode do you want to choose?\nAuto or Custom mode.", font=('Arial', 18))
        lb1.grid()
        
        bt_2 = tk.Button(div3, text='Auto Mode', font=('Arial', 14), bg='gray', fg='white', command=self.autoMode)
        bt_2.grid(sticky='e')
        bt_3 = tk.Button(div4, text='Custom Mode', font=('Arial', 14), bg='gray', fg='white', command=self.customMode)
        bt_3.grid(sticky='w')

        self.define_layout(self.window, cols=2, rows=3)
        self.define_layout([div1, div2, div3, div4])
        
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
        messagebox.showinfo('Burette Motor <info>', 'You choose the auto mode, press OK to start mixing.')
        # initial motor1 and motor2
        MOTOR1_STEPS, MOTOR2_STEPS = motor_param()
        SEQUENCE1, SEQUENCE_COUNT1, PIN_COUNT1 = motor_init(motor1)
        SEQUENCE2, SEQUENCE_COUNT2, PIN_COUNT2 = motor_init(motor2)
        # best ratio = 2:8 
        # maximum volume = 40
        DURATION1, DURATION2 = Mixing(10, 40)

        # start mixing
        motor_run(motor1, 1, DURATION1, MOTOR1_STEPS)
        motor_run(motor2, 1, DURATION2, MOTOR2_STEPS)
        messagebox.showinfo('Burette Motor <info>', 'Mixing finish.')

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
# %%
