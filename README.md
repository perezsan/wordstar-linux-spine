# wordstar-linux-spine
Wordstar Linux's Manjaro Linux aims to be a modular frontend and group of scripts that integrates Sublime Text 3 Install, 
Sublime Text's frontend (i.e. its build system or acces to bash scripts via keyboard shortcuts), along with wordsmith / pandoc ebook/pdf generation.
Possibly some other crap not mentioned, too, and most likely broken in some part (needs testing!)

**Requires Python3 and tk (tcl/tk.)**

**and Ruby / rubygem**

**[Wordsmith](https://github.com/perezsan/wordsmith)**

**And a Sublime Text 3 **

**(optional)** xmlstarlet for reference.odt title updating

clone project, chmod 700 install-spine.sh, then run ./install-spine.sh. Move spine dir wherever you like (I recommend ~/.config/spine), and add its location to your $PATH like this in ~/.profile, ~/.bashrc, and most positively, ~/.bash_profile :

**export SPINE_DIR="$HOME/.config/spine"**

**export PATH="$PATH:$SPINE_DIR"**

then run start-spine (you may need to log out of your desktop enviroment, and relog for settings to fully take affect

These set of scripts can be easily modified to work on any distro and/or desktop enviroment (or even lack thereof.)
Perhaps the goal will be to set it up as such, as these will probably only work under **Manjaro Linux 19.02**, or even Arch varients.

These were modified from scripts I've made over the years, and thought I'd share with the world. I've have them working between
various flavors of Linux concurrently (e.g. funtoo, mx linux, fedora VM) but gutted some of the references (i.e. funtoos chroot32 shit, some rvm checks) to clean up for debugging
a community-derived buildiso from Manjaro Gnome 3, which is close to beta release. Not sure where I can host it, though. But for now, enjoy.

## **TODO**
1. A proper install script
2. PDF, epub ebook generation should work, but everybody's setup is slightly different, I'd presume--especially if one opted to install rvm.

3. Missing one of the most important aspect ... sumblime text keyboard config... not sure how to implement this with git. Probably just add the file to asset dir, then user will have to copy over to the proper directory manually (but if they're using Manjaro, I could script it easily.) All in good time.
