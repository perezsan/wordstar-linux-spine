#!/usr/bin/python3
import subprocess
from tkinter import *
from tab_bindings import *
from tkinter import ttk

c1_var=StringVar(TAB2)
c1_var.set('No')

c2_var=StringVar(TAB2)
c2_var.set('No')


c3_var=StringVar(TAB2)
c3_var.set('No')


def use_encryption(ue):
	ue = print('Use Encryption:', c1_var.get())

def delete_project_after_archive(dpa):
	dpa = print('Delete Project Folder After Archive Project:', c2_var.get())
def delete_wips_after_archive(dwa):
	dwa = print('Delete WIPs Folder After Archive WIPs:', c3_var.get())

def start(choice):
	ue = c1_var.get()
	dpa = c2_var.get()
	dwa = c3_var.get()

	def debug_project_archive():
		print('-===========================-')
		print('Archive Type:', choice)
		print('Use Encryption:', ue)
		print('Delete Project Folder After Archiving Project Folder:', dpa)
		print('Delete WIPs Folder After Archiving Project Folder:', dwa)
		print('-===========================-')

	def debug_wip_archive():
		print('-===========================-')
		print('Archive Type:', choice)
		print('Use Encryption:', ue)
		print('Delete Project Folder After Archiving WIPs Folder:', dpa)
		print('Delete WIPs Folder After Archiving WIPs Folder:', dwa)
		print('-==========================-')

	def debug_archive_all():
		print('-===========================-')
		print('Archive Type:', choice)
		print('Use Encryption:', ue)
		print('Delete Project Folder After Archiving Everything:', dpa)
		print('Delete WIPs Folder After Archiving Everything:', dwa)
		print('-==========================-')


	############ Project Folder; No Selections ######
	if (choice=='markdown_only' and ue=='No' and dpa=='No' and dwa=='No'):
		print(debug_project_archive())
		subprocess.Popen(['wsl-archive-current-project'])
	############ Project Folder; Delete WIP Folder Only #####
	elif (choice=='markdown_only' and ue=='No' and dpa=='No' and dwa=='Yes'):
		print(debug_project_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-current-project' ' && ' \
			'wsl-delete-wips-folder'])
	############ Project Folder; Delete Project Folder After Archiving Project Folder ######
	elif (choice=='markdown_only' and ue=='No' and dpa=='Yes' and dwa=='No'):
		print(debug_project_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-current-project' ' && ' \
			'wsl-delete-project-folder'])
	############ Project Folder; Delete Project & WIP Folders After Archiving Project Folder #####
	elif (choice=='markdown_only' and ue=='No' and dpa=='Yes' and dwa=='Yes'):
		print(debug_project_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-current-project' ' && ' \
			'wsl-delete-project-folder' ' ; ' \
			'wsl-delete-wips-folder'])
	############ Project Folder; Encrypt; No other Selections ##########
	elif (choice=='markdown_only' and ue=='Yes' and dpa=='No' and dwa=='No'):
		print(debug_project_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-project'])
	############ Project Folder; Encrypt; Delete Project Folder After Archiving Project Folder #####
	elif (choice=='markdown_only' and ue=='Yes' and dpa=='Yes' and dwa=='No'):
		print(debug_project_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-project' ' && ' \
			'wsl-delete-project-folder'])
	############ Project Folder; Encrypt; Delete Project & WIP Folders After Archiving Project Folder ######
	elif (choice=='markdown_only' and ue=='Yes' and dpa=='Yes' and dwa=='Yes'):
		print(debug_project_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-project' ' && ' \
			'wsl-delete-project-folder' ' ; ' \
			'wsl-delete-wips-folder'])
	############ Project Folder; Encrypt; Delete WIP Folder Only After Archiving Project Folder
	elif (choice=='markdown_only' and ue=='Yes' and dpa=='No' and dwa=='Yes'):
		print(debug_project_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-project' ' && ' \
			'wsl-delete-wips-folder'])
	############ WIPS; No Selections ###################
	elif (choice=='wips_only' and ue=='No' and dpa=='No' and dwa=='No'):
		print(debug_wip_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-current-wips'])
	############ WIP Folder; Delete WIP Folder Only #####
	elif (choice=='wips_only' and ue=='No' and dpa=='No' and dwa=='Yes'):
		print(debug_wip_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-current-wips' ' && ' \
			'wsl-delete-wips-folder'])
	############ WIP Folder; Delete Project Folder After Archiving WIP Folder ######
	elif (choice=='wips_only' and ue=='No' and dpa=='Yes' and dwa=='No'):
		print(debug_wip_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-current-wips' ' && ' \
			'wsl-delete-project-folder'])
	############ WIP Folder; Delete Project & WIP Folders After Archiving WIP Folder #####
	elif (choice=='wips_only' and ue=='No' and dpa=='Yes' and dwa=='Yes'):
		print(debug_wip_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-current-wips' ' && ' \
			'wsl-delete-project-folder' ' ; ' \
			'wsl-delete-wips-folder'])
	############ WIP Folder; Encrypt; No other Selections ##########
	elif (choice=='wips_only' and ue=='Yes' and dpa=='No' and dwa=='No'):
		print(debug_wip_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-wips'])
	############ WIP Folder; Encrypt; Delete Project Folder After Archiving WIP Folder #####
	elif (choice=='wips_only' and ue=='Yes' and dpa=='Yes' and dwa=='No'):
		print(debug_wip_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-wips' ' && ' \
			'wsl-delete-project-folder'])
	############ WIP Folder; Encrypt; Delete Project & WIP Folders After Archiving WIP Folder ######
	elif (choice=='wips_only' and ue=='Yes' and dpa=='Yes' and dwa=='Yes'):
		print(debug_wip_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-wips' ' && ' \
			'wsl-delete-project-folder' ' ; ' \
			'wsl-delete-wips-folder'])
	############ WIP Folder; Encrypt; Delete WIP Folder Only After Archiving WIP Folder
	elif (choice=='wips_only' and ue=='Yes' and dpa=='No' and dwa=='Yes'):
		print(debug_wip_archive())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-wips' ' && ' \
			'wsl-delete-wips-folder'])
	########### \\\ ARCHIVE ALL /// No Selections ###################
	elif (choice=='archive_all' and ue=='No' and dpa=='No' and dwa=='No'):
		print(debug_archive_all())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-current-project' ' && ' \
			'wsl-archive-current-wips'])
	############ Archive ALL; Delete WIP Folder Only #####
	elif (choice=='archive_all' and ue=='No' and dpa=='No' and dwa=='Yes'):
		print(debug_archive_all())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-current-project' ' && ' \
			'wsl-archive-current-wips' ' ; ' \
			'wsl-delete-wips-folder'])
	############ Archive ALL; Delete Project Folder After Archiving Everything ######
	elif (choice=='archive_all' and ue=='No' and dpa=='Yes' and dwa=='No'):
		print(debug_archive_all())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-current-project' ' && ' \
			'wsl-archive-current-wips' ' ; ' \
			'wsl-delete-project-folder'])
	############ Archive ALL; Delete Project & WIP Folders After Archiving Everything #####
	elif (choice=='archive_all' and ue=='No' and dpa=='Yes' and dwa=='Yes'):
		print(debug_archive_all())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-current-project' ' && ' \
			'wsl-archive-current-wips' ' ; ' \
			'wsl-delete-project-folder' ' ; ' \
			'wsl-delete-wips-folder'])
	############ Archive ALL; Encrypt; No other Selections ##########
	elif (choice=='archive_all' and ue=='Yes' and dpa=='No' and dwa=='No'):
		print(debug_archive_all())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-project' ' && ' \
			'wsl-archive-encrypt-current-wips'])
	############ Archive ALL; Encrypt; Delete Project Folder After Archiving EVERYTING #####
	elif (choice=='archive_all' and ue=='Yes' and dpa=='Yes' and dwa=='No'):
		print(debug_archive_all())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-project' ' && ' \
			'wsl-archive-encrypt-current-wips' ' ; ' \
			'wsl-delete-project-folder'])
	############ Archive ALL; Encrypt; Delete Project & WIP Folders After Archiving Everything ######
	elif (choice=='archive_all' and ue=='Yes' and dpa=='Yes' and dwa=='Yes'):
		print(debug_archive_all())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-project' ' && ' \
			'wsl-archive-encrypt-current-wips' ' ; ' \
			'wsl-delete-project-folder' ' ; ' \
			'wsl-delete-wips-folder'])
	############ Archive ALL; Encrypt; Delete WIP Folder Only After Archiving Everything
	elif (choice=='archive_all' and ue=='Yes' and dpa=='No' and dwa=='Yes'):
		print(debug_archive_all())
		subprocess.Popen(['/bin/bash', '-c', 'wsl-archive-encrypt-current-project' ' && ' \
			'wsl-archive-encrypt-current-project' ' ; ' \
			'wsl-delete-wips-folder'])

	else:
		print("Make a selection and it will archive selection away (default is no encryption, unless you check the box.)")

