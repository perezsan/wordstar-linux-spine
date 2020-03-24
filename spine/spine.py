#!/usr/bin/python3
import os
import subprocess
import sys
import tkinter as tk
from tkinter import ttk

# intializing the window
window = tk.Tk()
window.title("Wordstar Linux Configurator - SPINE")
window.geometry('600x400')

# Color ttk via style
style = ttk.Style()
style.configure("Black.Tab", foreground="white", background="black")

sys.path.append("$SPINE_DIR/")

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
TAB_BINDINGS.add(TAB5, text='Advanced Configuration')
TAB_BINDINGS.pack(expand=1, fill="both")

###################
#Tab window contents i.e. buttons
#########################
# 1st tab definitions, mostly buttons
def openCheatSheet():
   print ("Opening Sublime Text Cheat Sheet...")
   subprocess.call('start-opencheatsheet', shell=True)


# Firewall on/off for gnome-pomodor checkbox
#definitions for firewallOff and firewallOn

def PomodoroFirewallOn():
   subprocess.call('toggle-pomodoro-firewall-on', shell=True)
def PomodoroFirewallOff():
   subprocess.call('toggle-pomodoro-firewall-off')

#1st tab - Fresh Install Help
ttk.Label(TAB1, text="Welcome to Wordstar Linux System Configurator",\
   style="Black.Tab").grid(column=0, row=0, padx=10, pady=10, columnspan=3)
ttk.Button(TAB1, text="Wordstar Linux: Getting Started...",\
   command = openCheatSheet).grid(column=0, row=6, padx=10, pady=10)

# configs
ttk.Label(TAB1, text="Project Name (New or Existing)", \
   style="").grid(column=0, row=1, padx=10, pady=20)
#Set Project Name
userin = ''
e = ttk.Entry(TAB1, textvariable=userin)
e.grid(column=1, row=1, padx=2, pady=0)

def process(event=None):
   content = e.get()
   print(content)
   subprocess.call('export TITLE="{}" && wsl-set-current-project-python'.format(content), shell=True)

# Set Author
ttk.Label(TAB1, text="Pen Name", \
   style="").grid(column=0, row=2, padx=10, pady=20)
userin2 = ''
f = ttk.Entry(TAB1, textvariable=userin2)
f.grid(column=1, row=2, padx=2, pady=0)

def process2(event=None):
   penname = f.get()
   print(penname)
   subprocess.call('export AUTHOR="{}" && wsl-change-author-python'.format(penname), shell=True)

# Set Email
ttk.Label(TAB1, text="Author\'s Email", \
   style="").grid(column=0, row=3, padx=10, pady=20)
userin3 = ''
g = ttk.Entry(TAB1, textvariable=userin3)
g.grid(column=1, row=3, padx=2, pady=0)

def process3(event=None):
   email = g.get()
   print(email)
   subprocess.call('export EMAIL="{}" && wsl-change-email-python'.format(email), shell=True)

e.bind('<Return>', process)
f.bind('<Return>', process2)
g.bind('<Return>', process3)


# Disable/enable firewall rules when using Gnome Pomodoro timers ...
#probably should leave it enabled if you want to get writing done!
firewallon = ttk.Radiobutton(TAB1, text="Enable Internet Blocking when Using Gnome Pomodoro", \
value=1,\
command = PomodoroFirewallOn).grid(column=0, row=4, padx=2, pady=10)
firewalloff = ttk.Radiobutton(TAB1, text="Disable Internet Blocking when Using Gnome Pomodoro", \
value=2,\
 command = PomodoroFirewallOff).grid(column=0, row=5, padx=2, pady=10)

### 2nd tab - Archive /rename utilities

#Archive Current Project and/or WIP folder ... with option for encryption
# value = StringVar()
# keepvalue = value.get()

# box = ttk.Combobox(TAB2, textvariable=keepvalue, state='readonly')
# box['values'] = ('Archive Project (with encryption)', \
#'Archive WIPs only (with encryption)', 'Archive Both (with encryption)')
# box.current(0)
# box.grid(column=0, row=0)


# Rename Project ... rename folder with $TITLE, and rename .wordsmith and metadata.xml files
ttk.Label(TAB2, text="Rename Current Project", \
   style="").grid(column=0, row=1, padx=2, pady=0)
rename_project = ''
i = ttk.Entry(TAB2, textvariable=rename_project)
i.grid(column=1, row=1, padx=2, pady=0)

def process5(event=None):
   renamedir = i.get()
   print(renamedir)
   subprocess.call('export TITLE_DIR_NEW="{}" && wsl-rename-current-project-python'.format(renamedir), shell=True)
i.bind('<Return>', process5)

#3rd tab - Install Writing Apps
def installSublimeStable():
   print ("Installing Sublime Text 3...")
   subprocess.call('start-install-sublime-text', shell=True)

def installSublimeNightly():
   print ("Installing Sublime Text 3 Nightly...")
   subprocess.call('start-install-sublime-text-nightly', shell=True)

ttk.Label(TAB3, text="Sublime Options", style="Black.Tab").grid(column=0, row=0, padx=10, pady=10)
ttk.Button(TAB3, text="Install Sublime Text 3", command = installSublimeStable).grid(column=0, row=1, padx=10, pady=10)
ttk.Button(TAB3, text="Install Sublime Text 3 Nightly", command = installSublimeNightly).grid(column=0, row=2, padx=10, pady=10)

#4th tab - Writing Utilities
def installPomodoro():
   print ("Installing Gnome Pomodoro...")
   subprocess.call('start-install-pomodoro', shell=True)

ttk.Button(TAB4, text="Install Gnome Pomodoro", command = installPomodoro).grid(column=0, row=0, padx=20, pady=10)

ttk.Label(TAB4, text="Note: After installation, \
 if gnome-pomodoro freezes up upon starting a timer", style="Black.Tab").grid(column=0, row=1, padx=10, pady=0)
ttk.Label(TAB4, text="Alt+F2, then type only the letter r,\
 then hit Return, and that should fix it for good.", font="", style="Black.Tab").grid(column=0, row=2, padx=2, pady=0)

#5th tab - Advanced Wordstar Linux Configuration
#Definitions for Advanced Folder Config --use at own risk!
ttk.Label(TAB5, text="Advanced Configuration: USE AT OWN RISK!",\
   style="Black.Tab").grid(column=1, row=0, padx=10, pady=10)
# Change SPINE_DIR
ttk.Label(TAB5, text="Set Spine Scripts Path (Use if downloaded scripts from git)", \
   style="").grid(column=0, row=3, padx=2, pady=0)
spine_dir = ''
h = ttk.Entry(TAB5, textvariable=spine_dir)
h.grid(column=1, row=3, padx=2, pady=0)

def process4(event=None):
   spinedir = h.get()
   print(spinedir)
   subprocess.call('export SPINE_DIR_NEW="{}" && wsl-change-spine-dir-python'.format(spinedir), shell=True)
h.bind('<Return>', process4)


tk.mainloop()

window.mainloop()
