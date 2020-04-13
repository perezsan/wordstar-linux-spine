# wordstar-linux-spine
*Spine* aims to be a distro agnostic frontend and suite of scripts that integrates Sublime Text 3 and its frontend (i.e. an in-app keybindings to access to bash scripts via keyboard shortcuts), along with wordsmith / pandoc ebook/pdf generation, and possibly some other crap not mentioned, too -- most likely broken in some parts (needs testing!) as it was initially designed for a dedicated Manjaro Linux custom iso.

**Requires Python3 and tk (tcl/tk.)**

**Ruby / rubygem** / or **RVM**

**[Wordsmith](https://github.com/perezsan/wordsmith)** (should auto-install when you run the install script.)

**pandoc**

**unoconv**

**xmlstarlet** ... for reference.odt title updating

**And a Sublime Text 3**

**(Somewhat optional)** libreoffice ... used to recalculate word count for pdf generation -- unfortunately hard coded right now, so just install it if you're not fussy (I'll fix it later.)

**(recommended)** calibre ... epubs should auto-open in either calibre or xdg-open user default (one of my scripts may set this to pcmanfm, as that is the default under Wordstar Linux Manjaro 19.02

**(optional)**  gnome pomodoro ... timer for writing ... firewall enabling is not enabled by default. user would have to have sudo and update /etc/sudoers to run firewall-on and firewall-off as root with nopasswd, then enable gnomepomodoro plugin to run scripts on play/pause/stop.

**(optional)** gpg2 for manuscrupt and WIP archive encryption

**(SIDEBAR)** A full working distro can be downloaded from here: [Wordstar Linux 19.02 Manjaro](https://healingrant.com/heaviside/wordstar-linux/)

______________________________

1. Run ./install-spine.sh. This should copy the spine dir to ~/.config/spine and add SPINE_DIR to PATH and as a var in ~/.profile, ~/.bashrc, and ~/.bash_profile. It should also fetch a copy of perezsan/wordsmith from git, then rake that bitch up in to a working bin for either rvm installs or run-of-the-mill rubygem setups.

2. Start-spine (you may need to log out of your desktop enviroment, and relog for settings to fully take affect

These set of scripts should work on any distro and/or desktop enviroment (or even lack thereof.)
The goal is to make this project as distro-agnostic as possible.

These were modified from scripts I've made over the years, and thought I'd share with the world. I've have them working between
various flavors of Linux concurrently (e.g. funtoo, mx linux, fedora VM) but gutted some of the references (i.e. funtoos chroot32 shit, some rvm checks) to clean up for debugging
a community-derived buildiso from Manjaro Gnome 3, which has been released (see  **SIDEBAR** link above.) 

## ** Known Issues **
1. Changing Cloud dir requires restart for changes to take affect.

## **TODO**
1. PDF, epub ebook generation should work out of the box, as the install script installs wordsmith from git, but everybody's setup is slightly different, I'd presume. I may have forgotten a dependancy...!

