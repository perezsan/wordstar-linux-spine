#!/bin/bash
chmod 700 spine/* \
&& chmod 700 spine/reticulation/install-* \
&& chmod 700 spine/reticulation/reopen-* \
&& chmod 700 spine/reticulation/set-caps-* \
&& chmod 700 spine/reticulation/wsl-setup* \
&& chmod 700 spine/reticulation/close-* \
&& sh -c spine/reticulation/wsl-setup
