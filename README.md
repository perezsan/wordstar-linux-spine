# wordstar-linux-spine
Wordstar Linux's *Spine* aims to be a modular frontend and suite of scripts that integrates Sublime Text 3 Install, 
Sublime Text's frontend (i.e. its build system or acces to bash scripts via keyboard shortcuts), along with wordsmith / pandoc ebook/pdf generation, and possibly some other crap not mentioned, too, and most likely broken in some part (needs testing!) because it was initially designed for a dedicated Manjaro Linux custom iso.

**Requires Python3 and tk (tcl/tk.)**

**and Ruby / rubygem** / or **RVM**

**[Wordsmith](https://github.com/perezsan/wordsmith)**

**pandoc**

**unoconv**

**And a Sublime Text 3 **

**(Somewhat optional)** libreoffice ... used to recalculate word count for pdf generation -- unfortunately hard coded right now, so just install it if you're not fussy (I'll fix it later.)

**(recommended)** xmlstarlet for reference.odt title updating

**(recommended)** calibre ... epubs should auto-open in either calibre or xdg-open user default (one of my scripts may set this to pcmanfm, as that is the default under Wordstar Linux Manjaro 19.02

**(recommended)**  gnome pomodoro ... timer for writing ... firewall enabling is not enabled by default. user would have to have sudo and update /etc/sudoers to run firewall-on and firewall-off as root with nopasswd, then enable gnomepomodoro plugin to run scripts on play/pause/stop.

**(SIDEBAR)** A full working distro can be downloaded from here: [Wordstar Linux 19.02 Manjaro](https://healingrant.com/heaviside/wordstar-linux/)

______________________________

1. Run ./install-spine.sh. This should copy the spine dir to ~/.config/spine and add SPINE_DIR to PATH and as a var in ~/.profile, ~/.bashrc, and ~/.bash_profile. It should also fetch a copy of perezsan/wordsmith from git, then rake that bitch up in to a working bin for either rvm installs or run-of-the-mill rubygem setups.

2. Start-spine (you may need to log out of your desktop enviroment, and relog for settings to fully take affect

These set of scripts can be easily modified to work on any distro and/or desktop enviroment (or even lack thereof.)
Perhaps the goal will be to set it up as such, as these will probably only work under **Manjaro Linux 19.02**, or even Arch variants.

These were modified from scripts I've made over the years, and thought I'd share with the world. I've have them working between
various flavors of Linux concurrently (e.g. funtoo, mx linux, fedora VM) but gutted some of the references (i.e. funtoos chroot32 shit, some rvm checks) to clean up for debugging
a community-derived buildiso from Manjaro Gnome 3, which is close to beta release. Not sure where I can host it, though. But for now, enjoy.

## **TODO**
1. PDF, epub ebook generation should work out of the box, as the install script installs wordsmith from git, but everybody's setup is slightly different, I'd presume. I may have forgotten a dependancy...!

2. Missing one of the most important aspect ... sumblime text keyboard config... not sure how to implement this with git. Probably just add the file to asset dir, then user will have to copy over to the proper directory manually (but if they're using Manjaro, I could script it easily.) All in good time.
