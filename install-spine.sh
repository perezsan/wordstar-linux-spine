#!/bin/bash

bashrc_check() {
if ls ~/.bashrc 1> /dev/null 2>&1; then
	echo 'export SPINE_DIR="$HOME/.config/spine"' >> ~/.bashrc \
	&& echo 'export PATH="$PATH:$SPINE_DIR"' >> ~/.bashrc
else
	touch ~/.bashrc \
	&& echo 'export SPINE_DIR="$HOME/.config/spine"' >> ~/.bashrc \
	&& echo 'export PATH="$PATH:$SPINE_DIR"' >> ~/.bashrc
fi
}

profile_check() {
if ls ~/.profile 1> /dev/null 2>&1; then
	echo 'export SPINE_DIR="$HOME/.config/spine"' >> ~/.profile \
	&& echo 'export PATH="$PATH:$SPINE_DIR"' >> ~/.profile
else
	touch ~/.profile \
	&& echo 'export SPINE_DIR="$HOME/.config/spine"' >> ~/.profile \
	&& echo 'export PATH="$PATH:$SPINE_DIR"' >> ~/.profile
fi
}

bash_profile_check() {
if ls ~/.bash_profile 1> /dev/null 2>&1; then
	echo 'export SPINE_DIR="$HOME/.config/spine"' >> ~/.bash_profile \
	&& echo 'export PATH="$PATH:$SPINE_DIR"' >> ~/.bash_profile
else
	touch ~/.bash_profile \
	&& echo 'export SPINE_DIR="$HOME/.config/spine"' >> ~/.bash_profile \
	&& echo 'export PATH="$PATH:$SPINE_DIR"' >> ~/.bash_profile
fi
}

if [[ -v SPINE_DIR ]]; then
	echo "Spine enviroment is already set to $SPINE_DIR"
else
	echo "Adding SPINE_DIR to ~/.profile ~/.bash_profile and ~/.bashrc" \
	&& profile_check \
	&& bash_profile_check \
	&& bashrc_check
fi

copy_spine() {
exec bash -c ./copy-spine-default-dir.sh
}

copy_spine
