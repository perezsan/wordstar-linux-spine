#!/bin/bash
source ~/.bashrc; \
cp -axrf spine "$HOME/.config" \
&& ~/.config/spine/reticulation/wsl-setup;
mkdir -p ~/.pandoc;
if ls ~/.pandoc/reference.odt 1> /dev/null 2>&1; then
	echo "~/.pandoc/reference.odt already exists .. you may have custom reference.odt already in place. Please copy ~/.config/spine/assets/reference.odt to ~/.pandoc if you want SPINE's standar manuscript format output" \
	&& cp ~/.config/spine/assets/*.xml ~/.pandoc/
else
	cp ~/.config/spine/assets/reference.odt ~/.pandoc/ \
	&& cp ~/.config/spine/assets/*.xml ~/.pandoc/
fi
echo "                                                              \
                                                                    \
-==[ Sublime Text 3 Keybindings install... Press ENTER to proceed ]==- \
                                                  Make sure you have installed sublime text 3 first before proceeding \
                                                  this section will overwrite any keybindings in ~/.config/sublime-text-3/Packages/User"  \
&& read \
&& echo ~/.config/sublime-text-3/Packages/User/ | xargs -p cp spine/assets/Default\ \(Linux\).sublime-keymap;
echo "                                                              \
                                                                    \
-==[ Libreoffice Macro Install.... Press ENTER to proceed ]==-      \
                                                  Make sure you have installed Libreoffice before proceeding         \
                                                  this section will overwrite any custom MACORS, which are usually stored in             \
                                                  ~/.config/libreoffice/4/user/basic/Standard                        \
                                                  If you answer N you will have to manually import the BASIC macro into Libreoffice yourself \
                                                   ... you can find the file in the assets dir as Recalculate.bas " \
&& read \
&& echo ~/.config/libreoffice/4/user/basic/Standard/ | xargs -p cp spine/assets/Module1.xba
