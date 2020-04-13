#!/bin/bash
source ~/.bashrc; \
cp -axrf spine "$HOME/.config" \
&& ~/.config/spine/reticulation/wsl-setup;
mkdir -p ~/.pandoc;
if ls ~/.pandoc/reference.odt 1> /dev/null 2>&1; then
	echo "file reference.odt already exists .. you may have custom reference.odt file already in place. please copy ~/.config/spine/assets/reference.odt to ~/.pandoc if you want SPINE's default manuscript output"
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
&& echo ~/.config/sublime-text-3/Packages/User/ | xargs -p cp spine/assets/Default\ \(Linux\).sublime-keymap
