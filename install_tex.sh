#!/usr/bin/bash

# Use Latex-Live, not apt, to install LaTex

tlmgrPackages() {
    ## evtl nur Heros https://www.gust.org.pl/projects/e-foundry/tex-gyre 
    sudo tlmgr install soulutf8 soul xcolor luatexbase luacode fontspec tex-gyre german babel-german hyphen-german
}

if command -v tlmgr &> /dev/null
then
    echo "tlmgr found"
    tlmgrPackages
else
    echo "tlmgr not found"
fi

#exit  ######################### be patient!! Only exit to test for new packages
direxists() {
    [ -d "$1" ]
}


if ! [[ -f install-tl-unx.tar.gz ]] && ! [[ -f install-tl-unx.tar ]]; then
    echo /// downloading installer...
    # TODO curl for macos
    wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
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
sudo install-tl-20??????/install-tl --scheme=basic --no-doc-install --no-src-install

#
# /usr/local/texlive/YYYY/bin/PLATFORM  in the Pfad !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ich habe die Optionen O / L gewählt !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# TODO do not require user input

echo /// installing required packages...
tlmgrPackages

