import glob
import os
import platform
import shutil
import sys

operatingSystem = platform.system()

def findExecutables():
    def couldbe(fpath):
        if os.path.isfile(fpath):
            return fpath
        else:
            return None

    if operatingSystem == 'Linux' or operatingSystem == 'Darwin':
        lualatex = shutil.which('lualatex')
        dvipdfmx = shutil.which('dvipdfmx')
        # Livetex may not install to path, therefore search at known locations
        if lualatex is None:
            for file in glob.iglob('/usr/local/texlive/**/bin/**/lualatex', recursive=True):
                lualatex = file
        if dvipdfmx is None:
            for file in glob.iglob('/usr/local/texlive/**/bin/**/dvipdfmx', recursive=True):
                dvipdfmx = file
        if operatingSystem == 'Darwin':
            # Livetex does not install to path, therefore search at known location
            if lualatex is None:
                lualatex = couldbe('/Library/TeX/texbin/lualatex')
            if dvipdfmx is None:
                dvipdfmx = couldbe('/Library/TeX/texbin/dvipdfmx')
    else:
        print('ERROR    system not covered')
        sys.exit(1)
    return lualatex, dvipdfmx


print( f'system     {operatingSystem}')

lualatex, dvipdfmx = findExecutables()
if lualatex is None or dvipdfmx is None:
    print('ERROR lualatex missing')
    sys.exit(2)

print( f'lualatex   {lualatex}')
print( f'dvipdfmx   {dvipdfmx}')
