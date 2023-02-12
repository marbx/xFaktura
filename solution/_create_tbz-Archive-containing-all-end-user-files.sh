##
## A tbz archive preserves the chmod of the files: the .command will stay executable
##

chmod 755 xFaktura.command

# tar-Option j means bzip2
tar cvfj xFaktura-Archive.tbz  xFaktura.command  xFaktura.py

echo WHAT IS INSIDE TBZ
tar tvf xFaktura-Archive.tbz
