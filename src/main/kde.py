from tkinter.ttk import Style
import tkinter as tk
from tkinter import ttk
from tkinter import *
from numpy import true_divide
import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import NULL, pandas2ri
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import csv
import subprocess
import multiprocessing

import heatmappage

LARGE_FONT = ("Bell Gothic Std Black", 40, 'bold')
MEDIUM_FONT = ("Bell Gothic Std Black", 25, 'bold')
BUTTON_FONT = ('Calibiri', 14, 'bold')
BACKGROUND_COLOR = '#407297'
LIGHT_BLUE = '#d4e1fa'


"""
Main page for KDE calculations
Allows user to select a file to run KDE calculations on
"""
class KDE_Page(tk.Frame):
    def __init__(self, parent, controller):
        self.filename = NULL
        self.tmp = tk.StringVar()
        self.tmp.set("hello")
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kernel Density Estimate", font=MEDIUM_FONT)
        label.pack(pady=10, padx=10)

        select_button = ttk.Button(self, text="Select File",
                                        command=lambda: self.select_file())
        select_button.pack()

        options_button = ttk.Button(self, text="Run KDE",
                                    command=lambda: self.get_parameters())
        options_button.pack()

        back_button = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(heatmappage.StartPage))
        back_button.pack()




    def select_file(self):
       # Tk.withdraw(self)
        self.filename = askopenfilename()

    def get_parameters(self):
        options_box = KDE_Calculation_Page(self.filename)
        options_box.wait_window(options_box)
        
        

"""
This page allows users to select parameters for KDE calculations and
run the KDE script
"""
class KDE_Calculation_Page(tk.Toplevel):
    def __init__(self, filename):
        tk.Toplevel.__init__(self)
        self.attributes('-topmost', 'true')

        self.filename = tk.StringVar()
        self.name_col = tk.StringVar()
        self.x_col = tk.StringVar()
        self.y_col = tk.StringVar()
        self.z_col = tk.StringVar()
        self.is_2d = tk.BooleanVar()
        self.is_2d.set(False)
        self.noise = tk.BooleanVar()
        self.noise.set(False)
        self.m = tk.IntVar()

        self.filename.set(filename)

        self.headers = self.get_headers(self.filename.get())
    
        name_col_label = tk.Label(self, text='Name Column', bg='white')
        name_col_label.pack()
        name_col_dropdown = tk.OptionMenu(self, self.name_col, *self.headers)
        name_col_dropdown.pack()

        x_col_label = tk.Label(self, text = "X Column", bg='white')
        x_col_label.pack()
        x_col_dropdown = tk.OptionMenu(self, self.x_col, *self.headers)
        x_col_dropdown.pack()

        y_col_label = tk.Label(self, text = "Y Column", bg='white')
        y_col_label.pack()
        y_col_dropdown = tk.OptionMenu(self, self.y_col, *self.headers)
        y_col_dropdown.pack()

        z_col_label = tk.Label(self, text = "Z Column", bg='white')
        z_col_label.pack()
        z_col_dropdown = tk.OptionMenu(self, self.z_col, *self.headers)
        z_col_dropdown.pack()

        m_label = tk.Label(self, text = "Scaling Factor (m)", bg='white')
        m_label.pack()
        m_slider = tk.Scale(self, from_=1, to=10, orient=HORIZONTAL, variable=self.m)
        m_slider.pack()

        is_2d_checkbox = tk.Checkbutton(self, text="Check here if data is 2D", variable=self.is_2d)
        is_2d_checkbox.pack()

        noise_checkbox = tk.Checkbutton(self, text='Add noise to data?', variable=self.noise)
        noise_checkbox.pack()
       
        tmp_button = tk.Button(self, text="Run KDE",
                                command=lambda: self.run_kde())
        tmp_button.pack()

    def get_headers(self, file):
        headers = list(pd.read_excel(file).columns)
        headers.append("N/A")
        return headers

    def create_options(self):
        options = {}
        options['name_col'] = self.name_col.get()

    def bool_to_str(self, b):
        if b:
            return 't'
        else:
            return 'f'

    def kde_thread_handler(self):
        kde_thread = multiprocessing.Process(target=self.run_kde)
        kde_thread.start()
        kde_thread.join()

    def run_kde(self):
        # r = robjects.r
        # r['source']('C:/Users/Kevin/Documents/GitHub/Zoo-Mapper/src/rscripts/3D_KDE_2021.R')

<<<<<<< HEAD
=======
        subprocess.call(['Rscript', './../rscripts/3D_KDE_2021.R',
                        self.filename, self.bool_to_str(self.is_2d.get()), self.name_col.get(), self.x_col.get(), self.y_col.get(), self.z_col.get()])
        print("done")







        
        
>>>>>>> 72a2318f232eddd601ae0ef9346f48fd9444f043

        print(self.m.get())
        subprocess.call(['Rscript', 'src/rscripts/3D_KDE_2021.R',
                        self.filename.get(), self.bool_to_str(self.is_2d.get()), self.name_col.get(), self.x_col.get(), self.y_col.get(), self.z_col.get(), self.bool_to_str(self.noise.get()), str(self.m.get())])

        print("done")

