#!/bin/bash
source ~/.bashrc; \
cp -axr spine "$HOME/.config" \
&& ~/.config/spine/reticulation/wsl-setup;
mkdir -p ~/.pandoc;
if ls ~/.pandoc/reference.odt 1> /dev/null 2>&1; then
	echo "file reference.odt already exists .. you may have custom reference.odt file already in place. please copy ~/.config/spine/assets/reference.odt to ~/.pandoc if you want SPINE's default manuscript output"
else
	cp ~/.config/spine/assets/reference.odt ~/.pandoc/ \
	&& cp ~/.config/spine/assets/*.xml ~/.pandoc/
fi

