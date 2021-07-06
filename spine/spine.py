#!/usr/bin/python3
import os
import subprocess
import sys
import tkinter as tk
from tkinter import ttk
#### pip3 install --user envbash if python throws you shit fitss
from envbash import load_envbash
## needed for StringVars
from tkinter import *
# intializing the window
from tab_bindings import *

sys.path.append("$SPINE_DIR/")
sys.path.append("$SPINE_DIR/reticulation/")

# Color ttk via style
# todo... fix_me ... create style.py and move any shits there
style = ttk.Style()
style.configure("Black.Tab", foreground="white", background="black")

# Load wsl profile through envbash to get BASH Variables for current project title only
# upon start-spine loading.
# ... Project Title is then updated to statusbar through textvariable='userinput' and command at end of (process) function

load_envbash('reticulation/gen_wordsmith_profile', remove=True)

project_title = (os.environ['TITLE'])
author_name = (os.environ['AUTHOR'])
author_email = (os.environ['EMAIL'])
wip_folder = (os.environ['WIP_DIR'])
wip_root = (os.environ['WIP_ROOT'])

###################
#Tab window contents i.e. buttons
#########################
# 1st tab definitions, mostly buttons
def openCheatSheet():
   print ("Opening Sublime Text Cheat Sheet...")
   subprocess.Popen(['start-opencheatsheet'])

# Firewall on/off for gnome-pomodor checkbox
#definitions for firewallOff and firewallOn

def PomodoroFirewallOn():
   subprocess.Popen(['toggle-pomodoro-firewall-on'])
def PomodoroFirewallOff():
   subprocess.Popen(['toggle-pomodoro-firewall-off'])

# Spine Configurator on/off autostarter checkbox
#definitions for SpineOn SpineOFf

def SpineOn():
   subprocess.Popen(['toggle-spine-autostart-on'])
def SpineOff():
   subprocess.Popen(['toggle-spine-autostart-off'])

#1st tab - Main Functions put on 1st tab so user doesn't have to wander tabs much or at all
##### TAB1 Section Titles ######

ttk.Label(TAB1, text="Create / Modify Project Profile",\
   style="Black.Tab").grid(column=1, row=0, padx=10, pady=10, columnspan=8, sticky=tk.E+tk.W)
ttk.Button(TAB1, text="Help . . .",\
   command = openCheatSheet).grid(column=4, row=4, padx=20, pady=10, columnspan=3)
##################### Set Project Name #############
ttk.Label(TAB1, text="Project Name (New or Existing)", \
   style="").grid(column=2, row=1, padx=10, pady=20)

userinput = ''
project = ttk.Entry(TAB1, textvariable=userinput)
project.grid(column=3, row=1, padx=2, pady=0)

class Project:
	def __init__(self):
		pass
	def openFolder(event):
		manu_folder = (os.environ['MANU_DIR'])
		subprocess.Popen(['xdg-open', manu_folder])
	def setCurrent(event=None):
		content = project.get()
		subprocess.Popen(['/bin/bash', '-c','export TITLE="{}"' ' && ' \
			'wsl-set-current-project'.format(content)])
		statusbar.config(text='Current Project:  '+str(content))
		content_dir=content.replace(" ","_")
		format_folder = (os.environ['FORMAT_DIR'])
		new_project_folder = format_folder+content_dir
		statusbar.unbind("<Button-1>")
		def updateFolder(event):
			subprocess.Popen(['xdg-open', new_project_folder])
		statusbar.bind("<Button-1>", updateFolder)

		statusbar4.unbind("<Buttion-1>")
		wip_root = (os.environ['WIP_ROOT'])
		new_wip_dir = wip_root+content_dir
		statusbar4.config(text='Output Dir:  '+str(new_wip_dir))

		def clickWipFolder(event):
			subprocess.Popen(['xdg-open', new_wip_dir])
		statusbar4.bind("<Button-1>", clickWipFolder)

project.bind('<Return>', Project.setCurrent)

##################### Set Author ##########
ttk.Label(TAB1, text="Pen Name", \
   style="").grid(column=2, row=2, padx=10, pady=20)
userinput2 = ''
author = ttk.Entry(TAB1, textvariable=userinput2)
author.grid(column=3, row=2, padx=2, pady=0)

def setAuthor(event=None):
   penname = author.get()
   print(penname)
   subprocess.Popen(['/bin/bash', '-c','export AUTHOR="{}"' ' && ' \
	'wsl-change-author'.format(penname)])
   statusbar_author.config(text='Pen Name:  '+str(penname))
author.bind('<Return>', setAuthor)

##################### Set Email ############
ttk.Label(TAB1, text="Author\'s Email", \
   style="").grid(column=2, row=3, padx=10, pady=20)
userinput3 = ''
email = ttk.Entry(TAB1, textvariable=userinput3)
email.grid(column=3, row=3, padx=2, pady=0)

def setEmail(event=None):
   authoremail = email.get()
   print(email)
   subprocess.Popen(['/bin/bash', '-c','export EMAIL="{}"' ' && ' \
	'wsl-change-email'.format(authoremail)])
   statusbar_email.config(text='Email:  '+str(authoremail))

email.bind('<Return>', setEmail)

### 2nd tab - Archive /rename utilities
#Archive Current Project and/or WIP folder ... with option for encryption
# invoking archive_start.py that's in spine dir
from archive_start import *

ttk.Label(TAB2, text=". . . Archive Options . . .", \
	style="Black.Tab").grid(column=2, row=0, padx=0, pady=0, sticky=tk.E+tk.W)

c1 = ttk.Checkbutton(TAB2, text='Use Encryption', \
	var=c1_var, onvalue='Yes', offvalue='No',command=lambda: use_encryption(var.get())) \
	.grid(column=2, row=1, padx=0, pady=0)

c2 = ttk.Checkbutton(TAB2, text='Delete Project Folder After Archiving', \
	var=c2_var, onvalue='Yes', offvalue='No',command=lambda: delete_project_after_archive(var.get())) \
	.grid(column=2, row=2, padx=0, pady=0)

c3 = ttk.Checkbutton(TAB2, text='Delete WIPs Folder After Archiving', \
	var=c3_var, onvalue='Yes', offvalue='No',command=lambda: delete_project_after_archive(var.get())) \
	.grid(column=2, row=3, padx=0, pady=0)

# var StringVar for Archive Current. . .
var=StringVar(TAB2)
var.set(None)
ttk.Label(TAB2, text="Archive Current. . .", style="Black.Tab").grid(column=0, row=0, padx=0, pady=0, sticky=tk.E+tk.W)
ttk.Radiobutton(TAB2, text='Project Folder', value='markdown_only', variable=var) \
	.grid(column=0, row=1, padx=2, pady=0)
ttk.Radiobutton(TAB2, text='WIPs (e.g. pdf, epub output)', value='wips_only', variable=var) \
	.grid(column=0, row=2, padx=2, pady=0)
ttk.Radiobutton(TAB2, text='Project and WIPs Folders', value='archive_all', variable=var) \
	.grid(column=0, row=3, padx=2, pady=0)
ttk.Button(TAB2, text='Archive', command=lambda: start(var.get())) \
	.grid(column=1, row=2, padx=5, pady=0)

# Rename Project ... rename folder with $TITLE, and rename .wordsmith and metadata.xml files
ttk.Label(TAB1, text="Rename Current Project", \
   style="").grid(column=2, row=4, padx=20, pady=20)
rename_project = ''
i = ttk.Entry(TAB1, textvariable=rename_project)
i.grid(column=3, row=4, padx=2, pady=0)

def renameCurrentProject(event=None):
	renameproject = i.get()
	print(renameproject)
	subprocess.Popen(['/bin/bash', '-c','export TITLE_DIR_NEW="{}"' ' && ' \
		'wsl-rename-current-project'.format(renameproject)])
	statusbar.config(text='Current Project:'+str(renameproject))
	renameproject_dir=renameproject.replace(" ","_")
	format_folder = (os.environ['FORMAT_DIR'])
	renamed_project_folder = format_folder+renameproject_dir
	statusbar.unbind("<Button-1>")
	def clickRenamedFolder(event):
		subprocess.Popen(['xdg-open', renamed_project_folder])
	statusbar.bind("<Button-1>", clickRenamedFolder)

	statusbar4.unbind("<Buttion-1>")
	wip_root = (os.environ['WIP_ROOT'])
	new_wip_dir = wip_root+renameproject_dir
	statusbar4.config(text='Output Dir:  '+str(new_wip_dir))
	def clickWipFolder(event):
		subprocess.Popen(['xdg-open', new_wip_dir])
	statusbar4.bind("<Button-1>", clickWipFolder)
i.bind('<Return>', renameCurrentProject)

ttk.Label(TAB2, text="Quick and Dirty Backup",\
   style="Black.Tab").grid(column=0, row=8, padx=10, pady=10, columnspan=5, sticky=tk.E+tk.W)

def archive_everything():
   print ("Backup All Projects & WIPs")
   subprocess.Popen(['wsl-archive-everything'])
ttk.Button(TAB2, text="Backup All Projects & WIPs", command = archive_everything).grid(column=1, row=9, padx=10, pady=10)

def archive_encrypt_everything():
   print ("Backup All Projects & WIPs (with Encryption)")
   subprocess.Popen(['wsl-archive-encrypt-everything'])
ttk.Button(TAB2, text="Backup All Projects & WIPs (with Encryption)", command = archive_encrypt_everything).grid(column=1, row=10, padx=10, pady=10)

#3rd tab - Install Writing Apps
def installSublimeStable():
   print ("Installing Sublime Text 3...")
   subprocess.Popen(['start-install-sublime-text'])

def installSublimeNightly():
   print ("Installing Sublime Text 3 Nightly...")
   subprocess.Popen(['start-install-sublime-text-nightly'])

ttk.Label(TAB3, text="Sublime Options", style="Black.Tab").grid(column=0, row=0, padx=0, pady=0)
# ttk.Button(TAB3, text="Install Sublime Text 3", command = installSublimeStable).grid(column=0, row=1, padx=10, pady=10)
ttk.Button(TAB3, text="Install Sublime Text 3 Nightly", command = installSublimeNightly).grid(column=0, row=2, padx=10, pady=10)

#4th tab - Writing Utilities
def installPomodoro():
   print ("Installing Gnome Pomodoro...")
   subprocess.Popen(['start-install-pomodoro'])

ttk.Button(TAB4, text="Install Gnome Pomodoro", command = installPomodoro).grid(column=0, row=0, padx=20, pady=10)

ttk.Label(TAB4, text="Note: After installation, \
 if gnome-pomodoro freezes up upon starting a timer", style="Black.Tab").grid(column=0, row=1, padx=10, pady=0)
ttk.Label(TAB4, text="Alt+F2, then type only the letter r,\
 then hit Return, and that should fix it for good.", font="", style="Black.Tab").grid(column=0, row=2, padx=2, pady=0)

#5th tab - Advanced Wordstar Linux Configuration
#Definitions for Advanced Folder Config --use at own risk!
ttk.Label(TAB5, text="Startup Configuration",\
   style="Black.Tab").grid(column=0, row=0, padx=10, pady=10, sticky=tk.E+tk.W)


# Disable/enable Autostarting of
#Wordstar Linux Spine Configurator upon boot
spineon = ttk.Radiobutton(TAB5, text="Autostart Spine", \
value=1,\
command = SpineOn).grid(column=0, row=1, padx=2, pady=10)
spineoff = ttk.Radiobutton(TAB5, text="Disable Spine Upon Login", \
value=2,\
 command = SpineOff).grid(column=0, row=2, padx=2, pady=10)

ttk.Label(TAB5, text="Cloud Directory (Default:  $HOME/Sync)", \
   style="").grid(column=0, row=5, padx=2, pady=0)
cloud_dir = ''
newclouddir = ttk.Entry(TAB5, textvariable=cloud_dir)
newclouddir.grid(column=1, row=5, padx=2, pady=0)

def changeCloudDir(event=None):
	clouddir = newclouddir.get()
	print(clouddir)
	subprocess.Popen(['/bin/bash', '-c','export CLOUD_DIR_NEW="{}"' ' && ' \
		'wsl-change-cloud-dir' ' && ' \
		'start-gen-wordsmith-project'.format(clouddir)])
	title = (os.environ['TITLE'])
	new_manu_folder = (os.environ['NEW_MANU_DIR'])
	cloud_dir=clouddir.replace(" ","_")
	title_dir=title.replace(" ","_")
	renamed_sync_folder = cloud_dir+new_manu_folder+title_dir
	statusbar.config(text='Current Project: '+str(title))
	statusbar.unbind("<Button-1>")
	def clickRenamedCloudFolder(event):
		subprocess.Popen(['xdg-open', renamed_sync_folder])
	statusbar.bind("<Button-1>", clickRenamedCloudFolder)

	statusbar4.unbind("<Buttion-1>")
	project_root = (os.environ['PROJECT_ROOT'])
	new_wip_dir = cloud_dir+'/'+project_root+'/WIPs/'+title_dir
	statusbar4.config(text='Output Dir:  '+str(new_wip_dir))
	def clickWipFolder(event):
		subprocess.Popen(['xdg-open', new_wip_dir])
	statusbar4.bind("<Button-1>", clickWipFolder)
newclouddir.bind('<Return>', changeCloudDir)

# Disable/enable firewall rules when using Gnome Pomodoro timers ...
#probably should leave it enabled if you want to get writing done!
ttk.Label(TAB5, text="Advanced Configuration",\
   style="Black.Tab").grid(column=0, row=4, padx=10, pady=10, columnspan=5, sticky=tk.E+tk.W)
ttk.Label(TAB5, text="Pomodoro Integration",\
   style="Black.Tab").grid(column=3, row=0, padx=10, pady=10, sticky=tk.E+tk.W)
firewallon = ttk.Radiobutton(TAB5, text="Enable Internet Blocking", \
value=1,\
command = PomodoroFirewallOn).grid(column=3, row=1, padx=2, pady=0)
firewalloff = ttk.Radiobutton(TAB5, text="Disable Internet Blocking", \
value=2,\
 command = PomodoroFirewallOff).grid(column=3, row=2, padx=2, pady=0)

# Status Bar and its updates to any change in Project Title, Author, or email, etc
openFolder = Project.openFolder
statusbar = tk.Label(window, bd=1, relief=tk.SUNKEN, anchor=tk.N,text='Current Project:  '+str(project_title), font='bold')
statusbar.pack(side=tk.TOP, fill=tk.X)
statusbar.bind("<Button-1>", openFolder)

# author / penname status
statusbar_author = tk.Label(window, bd=1, relief=tk.SUNKEN, anchor=tk.W,text='Pen Name:  '+str(author_name))
statusbar_author.pack(side=tk.LEFT, fill=tk.X)
# Email
statusbar_email= tk.Label(window, bd=1, relief=tk.SUNKEN, anchor=tk.W,text='Email:  '+str(author_email))
statusbar_email.pack(side=tk.RIGHT, fill=tk.X)

# WIP Folder .. click to open it
def clickWipFolder(event):
	wip_folder = (os.environ['WIP_DIR'])
	subprocess.Popen(['xdg-open', wip_folder])
statusbar4= tk.Label(window, bd=1, relief=tk.SUNKEN, \
	anchor=tk.S,text='Output Dir:  '+str(wip_folder))
statusbar4.pack(side=tk.BOTTOM, fill=tk.X)
statusbar4.bind("<Button-1>", clickWipFolder)

window.iconphoto(False, tk.PhotoImage(file='./assets/Wordstar.png'))

window.mainloop()
