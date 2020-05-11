## the tk gui for our program.

from tkinter import *
from tkinter import ttk
from controller import Control

class View:
    def __init__(self, master):
        self.master = master 
        self.master.geometry("300x300")
        self.master.grid()

        self.make_menu()
        
        test_choices = ['GoRaleigh', 'GoTriangle', 'Wolfline']
        self.agency_selector(test_choices) 

        self.route_selector([1, 2, 3])


    def make_menu(self):
        # creates the control menu.
        menubar = Menu(self.master)
        menubar.add_command(label='Set/Update API Key', command=Control.update_api_key)
        menubar.add_command(label='Quit', command=self.master.quit)
        self.master.config(menu=menubar)

    def agency_selector(self, agencies):
        # creates our agency combobox.
        agency_menu = ttk.Combobox(self.master, values=agencies, state='readonly') 
        agency_menu.grid(row=0, column=0)

    def route_selector(self, routes):
        # creates the route combobox.
        route_menu = ttk.Combobox(self.master, values=routes, state='readonly') 
        route_menu.grid(row=1, column=0)