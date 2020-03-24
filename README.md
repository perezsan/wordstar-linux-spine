# wordstar-linux-spine
Wordstar Linux's Manjaro Linux Frontend and group of scripts that integrates Sublime Text 3 Install, 
Sublime Text's frontend with wordsmith / pandoc ebook/pdf generation.
Possibly some other crap not mentioned, too!

**Requires Python3 and tk (tcl/tk.)**

**and Ruby / rubygem**

**And a Sublime Text 3 distro-specific install if not using Manjaro/arch**

clone project, then run ./install-spine.sh. Move spine dir wherever you like (I recommend ~/.config/spine), and add its location to your $PATH, then run Spine.py.

Under **Advanced tab** you can set the spine scripts dir to whatever you like (it will update your ~/.profile and ~/.bashrc to source ~/.profile_spine **but not move the actual dir!**)

These set of scripts can be easily modified to work on any distro and/or desktop enviroment (or even lack thereof.)
Perhaps the goal will be to set it up as such, as these will probably only work under **Manjaro Linux 19.02**, or even Arch varients.

These were modified from scripts I've made over the years, and thought I'd share with the world. I've have them working between
various flavors of Linux concurrently (e.g. funtoo, mx linux, fedora VM) but gutted some of the references (i.e. funtoos chroot32 shit, some rvm checks) to clean up for debugging
a community-derived buildiso from Manjaro Gnome 3, which is close to beta release. Not sure where I can host it, though. But for now, enjoy.
