# Use Latex-Live, not apt, to install LaTex

direxists() {
    [ -d "$1" ]
}
if ! [[ -f install-tl-unx.tar.gz ]] && ! [[ -f install-tl-unx.tar ]]; then
    echo downloading installer...
    wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
fi


if [[ -f install-tl-unx.tar.gz ]] && ! [[ -f install-tl-unx.tar ]]; then
    echo unzipping installer...
    gunzip install-tl-unx.tar.gz
fi


if ! direxists install-tl-20??????  &&  [[ -f install-tl-unx.tar ]]; then
    echo untaring installer...
    tar xf install-tl-unx.tar
fi

# DOCU https://tug.org/texlive/quickinstall.html
# Installtion macht web-download egal ob schon alles da!
echo installing...
sudo install-tl-20??????/install-tl --scheme=basic --no-doc-install --no-src-install

#
# /usr/local/texlive/YYYY/bin/PLATFORM  in the Pfad !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ich habe die Optionen O / L gewählt !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

## install the required packages
sudo tlmgr install soulutf8
sudo tlmgr install soul
sudo tlmgr install xcolor
sudo tlmgr install luatexbase
sudo tlmgr install luacode
sudo tlmgr install fontspec

## install the required fonts
sudo tlmgr install collection-fontsrecommended

## install German
sudo tlmgr install german
sudo tlmgr install babel-german


