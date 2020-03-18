#!/usr/bin/python3
import tkinter
import subprocess

top = tkinter.Tk()

def installSublimeNightly():
   print ("Installing Sublime Text 3 Nightly...")
   subprocess.call('$HOME/.scripts/start-install-sublime-text', shell=True)

def openCheatSheet():
   print ("Opening Sublime Text Cheat Sheet...")
   subprocess.call('$HOME/.scripts/start-opencheatsheet', shell=True)

def installPomodoro():
   print ("Below is the output from the shell script in terminal")
   subprocess.call('$HOME/.scripts/start-install-pomodoro', shell=True)

def changeProject():
   print ("What lovely idea you going to work on now!?")
   subprocess.call('$HOME/.scripts/start-wsl-set-current-project-name', shell=True)

B = tkinter.Button(top, text ="Install Sublime Text Nightly", command = installSublimeNightly)
C = tkinter.Button(top, text ="Wordstar Linux: Sublime Text Cheat Sheet ", command = openCheatSheet)
D = tkinter.Button(top, text ="Install Gnome Pomodoro", command = installPomodoro)
E = tkinter.Button(top, text ="Set Project Name -- i.e. what lovely manuscript would you like to work on now, Senior Pussycat?", command = changeProject)

B.pack()
C.pack()
D.pack()
E.pack()
top.mainloop()
