#!/usr/bin/python3
from tkinter import ttk
import tkinter as tk

window = tk.Tk()
window.title("Wordstar Linux Configurator - SPINE")
window.geometry('800x500')

#Call the tab framework
TAB_BINDINGS = ttk.Notebook(window)
#Welcome / readme 1st tab
TAB1 = ttk.Frame(TAB_BINDINGS)
TAB_BINDINGS.add(TAB1, text='Main')
# Archive /Rename Project Tab
TAB2 = ttk.Frame(TAB_BINDINGS)
TAB_BINDINGS.add(TAB2, text='Archive')
TAB_BINDINGS.pack(expand=1, fill="both")
#INstall writing apps
TAB3 = ttk.Frame(TAB_BINDINGS)
TAB_BINDINGS.add(TAB3, text='Install Writing Apps')
TAB_BINDINGS.pack(expand=1, fill="both")
#Writing Utilities
TAB4 = ttk.Frame(TAB_BINDINGS)
TAB_BINDINGS.add(TAB4, text='Install Writing Utilities')
TAB_BINDINGS.pack(expand=1, fill="both")

#Advanced Configuration i.e. change author name, change project title, change cloud dir, change root install dir
TAB5 = ttk.Frame(TAB_BINDINGS)
TAB_BINDINGS.add(TAB5, text='Configuration')
TAB_BINDINGS.pack(expand=1, fill="both")

