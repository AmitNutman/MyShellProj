import os
import sys


#always has at least 1 param with file name(ls.py). the second param is what it got
if len(sys.argv) == 2:
    #recive the params from bat - the path to read files from
    param_path = sys.argv[1]

    #checks if the path exists and if it is a folder(directory)
    if os.path.isdir(param_path):
        os.system(f'dir "{param_path}"')
    else:
        print("couldn't find folder")

#only one param - the file name(ls.py)
elif len(sys.argv) == 1:
    os.system("dir")

else:
    print("too many params")

