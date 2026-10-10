import os
import sys


#always has at least 1 param with file name(hexdump.py). the second param is what it got
if len(sys.argv) == 2:
    #recive the params from bat - the path to make into hex
    param_path = sys.argv[1]

    #checks if the path exists
    if os.path.exists(param_path):
        with open(param_path, "r") as file:
            content = file.read()
        #encoding from str - so we can make it to hex
        print(content.encode().hex())

    else:
        print("couldn't find file")

#if there are too many params / no params at all
else:
    print("needs 1 param exactly - file path")

