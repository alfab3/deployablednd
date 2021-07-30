try:
    from Tkinter import *
    import Tkinter as tk
except ImportError:
    from tkinter import *
    import tkinter as tk

mainWindow = Tk()

class Window(Frame):

    def __init__(self, master = None):
        #Initializes all Tkinter functions
        Frame.__init__(self, master)
        self.master = master
        self.init_window()#main window and menu bar
        self.main_widgets()#objects that inhabit the main page

    def init_window(self):
        self.master.title('D&D Character Sheet')

        #cascae menus
        menu = Menu(mainWindow)
        mainWindow.config(menu = menu)

        #file cascade menu
        file_C = Menu(menu)
        file_C.add_command(label='Exit', command = self.close_window)
        menu.add_cascade(label='File', menu=file_C)

        #windows cascade menu
        #opens other pop-up windows
        windows_C = Menu(menu)
        menu.add_cascade(label='Windows',menu=windows_C)

    def main_widgets(self):

    def open_new_character(self):
        newCharWindow = Toplevel(mainWindow)

        newCharWindow.title('Advanced Options')

        newCharWindow.geometry("650x300")

    def close_window(self):
        exit()
