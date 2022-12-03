##
## A tbz archive preserves the chmod of the files: the .command will stay executable
##

chmod 755 xFaktura.command

# tar-Option j means bzip2
tar cvfj xFaktura-Archive.tbz  Praxis1-Rechnung.tex  Praxis1.xlsx  xFaktura.command  xFaktura.py

echo test?
tar tvf xFaktura-Archive.tbz
