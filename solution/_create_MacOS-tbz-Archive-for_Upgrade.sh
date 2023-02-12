##
## A MacOS tbz archive preserves the chmod of the files: the .command will stay executable
##
# .tbz is an Archiv only for MacOS
# .command executes a command only on MacOS
#
# tar cjf archive.tbz singlefile
#  c create
#  j bzip2
#  f file
#
# tar xf archive.tbz
#  x extract
#  f file
#
# https://stackoverflow.com/questions/60593486/how-to-distribute-an-application-for-mac-os-so-that-it-can-be-run-by-double-clic


chmod 755 xFaktura.command

tar cvfj xFaktura-Archive.tbz  xFaktura.command xFaktura.py

echo .TBZ CONTENT
tar tvf xFaktura-Archive.tbz
