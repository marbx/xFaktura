

if ! [[ -f install-tl-unx.tar.gz ]] && ! [[ -f install-tl-unx.tar ]]; then
    echo getting installer
    wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
fi


if [[ -f install-tl-unx.tar.gz ]] && ! [[ -f install-tl-unx.tar ]]; then
    echo unzipping installer
    gunzip install-tl-unx.tar.gz
fi


if [[ -f install-tl- ]] && ! [[ -f install-tl-unx.tar ]]; then
    echo untar installer
    #tar xf install-tl-unx.tar
fi

# DOCU https://tug.org/texlive/quickinstall.html
#
# AUSPROBIEREN
# install-tl --scheme=scheme-basic

#sudo install-tl-20220724/install-tl -profile texlive.profile
#sudo install-tl-20220724/install-tl

# /usr/local/texlive/YYYY/bin/PLATFORM  in the Pfad
# ich habe die L option gewählt

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


