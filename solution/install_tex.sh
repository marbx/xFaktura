#!/usr/bin/env bash

# Use Latex-Live, not apt, to install LaTex

if command -v lualatex &> /dev/null
then
  echo found lualatex `lualatex --version | head -n 1`
  file -b `which lualatex`
  exit
fi


if command -v tlmgr &> /dev/null
then
    echo See `tlmgr list --only-installed | wc -l` TeXLive packages with tlmgr list --only-installed
else
    echo TeXLive Manager "tlmgr" not found
    echo THIS SCRIPT SHOULD RUN  tlmgr THE TEX LIVE MANAGER
    echo IN tlmgr, PRESS s=Schema, THEN PRESS d=basic !!!!
fi

echo exiting now, TODO when to install what?
exit

direxists() {
    [ -d "$1" ]
}


if ! [[ -f install-tl-unx.tar.gz ]] && ! [[ -f install-tl-unx.tar ]]; then
    echo /// downloading installer...
    curl -O --location  https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
fi


if [[ -f install-tl-unx.tar.gz ]] && ! [[ -f install-tl-unx.tar ]]; then
    echo /// unzipping installer...
    gunzip install-tl-unx.tar.gz
fi


if ! direxists install-tl-20??????  &&  [[ -f install-tl-unx.tar ]]; then
    echo /// untaring installer...
    tar xf install-tl-unx.tar
fi

# DOCU https://tug.org/texlive/quickinstall.html
# Installtion macht web-download egal ob schon alles da!
echo /// installing...
sudo install-tl-20*/install-tl --scheme=basic --no-doc-install --no-src-install

#
# /usr/local/texlive/YYYY/bin/PLATFORM  in the Pfad !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# I have to select Option O / L  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# TODO do not require user input

InstallTlmgrPackages() {
    ## evtl nur Heros https://www.gust.org.pl/projects/e-foundry/tex-gyre
    sudo tlmgr install soulutf8 soul xcolor luatexbase luacode fontspec tex-gyre german babel-german hyphen-german
}

echo /// installing required packages...
InstallTlmgrPackages

echo Adding texlive to the command PATH !!!!
export PATH=/usr/local/texlive/2022/bin/x86_64-linux:$PATH
