import platform
import shutil
import glob
import os


def findExecutables():
    operatingSystem = platform.system()
    if operatingSystem == 'Linux':
        lualatex = shutil.which('lualatex')
        dvipdfmx = shutil.which('dvipdfmx')
        # Livetex may not install to path, therefore search at known locations
        if lualatex is None:
            for file in glob.iglob('/usr/local/texlive/**/bin/**/lualatex', recursive=True):
                lualatex = file
        if dvipdfmx is None:
            for file in glob.iglob('/usr/local/texlive/**/bin/**/dvipdfmx', recursive=True):
                dvipdfmx = file
        if lualatex is None or dvipdfmx is None:
            print('ERROR    no lualatex or dvipdfmx')
    elif operatingSystem == 'Darwin':
        # Livetex does not install to path, therefore search at known location
        lualatex = '/Library/TeX/texbin/lualatex'
        dvipdfmx = '/Library/TeX/texbin/dvipdfmx'
        if not os.path.isfile(lualatex): lualatex = None
        if not os.path.isfile(dvipdfmx): dvipdfmx = None
    else:
        print('ERROR    system not covered')

    if not os.path.isfile(lualatex): print('ERROR    no lualatex')
    if not os.path.isfile(dvipdfmx): print('ERROR    no dvipdfmx')
    print( f'system     {operatingSystem}')
    print( f'lualatex   {lualatex}')
    print( f'dvipdfmx   {dvipdfmx}')



findExecutables()
