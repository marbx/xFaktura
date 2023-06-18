#!/usr/bin/env bash

# Use Latex-Live, not apt, to install LaTex


if command -v lualatex &> /dev/null
then
  echo found lualatex `lualatex --version | head -n 1`
  file -b `which lualatex`
  #exit
fi


if command -v tlmgr &> /dev/null
then
    echo See `tlmgr list --only-installed | wc -l` TeXLive packages with tlmgr list --only-installed
else
    echo TeXLive Manager "tlmgr" not found
    echo This script will now download and install tlmgr, the tex live manager
fi



if ! [[ -f install-tl-unx.tar.gz ]]; then
    echo /// downloading installer...
    curl -O --location  https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
fi


if [[ -f install-tl-unx.tar.gz ]]; then
    echo /// unzipping installer...
    gunzip --force --keep install-tl-unx.tar.gz
fi


echo /// untaring installer...
tar xf install-tl-unx.tar


# option --no-installation
INSTALLSTRING='sudo install-tl-20*/install-tl  --scheme=basic --no-doc-install --no-src-install --profile install_tex.profile'


# DOCU https://tug.org/texlive/quickinstall.html
# Installtion macht web-download egal ob schon alles da!
echo /// installing basic TexLive...
echo $INSTALLSTRING
$INSTALLSTRING

echo /// Checking tlmgr version...
tlmgr version


#
# DOC https://www.tug.org/texlive/doc/install-tl.html
echo /// Calling the TeX Live Manager...
TLMGRSTRING='sudo tlmgr install soul xcolor luatexbase luacode fontspec tex-gyre german babel-german hyphen-german setspace'
echo $TLMGRSTRING
$TLMGRSTRING
