import sys
import os


#always has at least 1 param with file name(grep.py). the second and third param is what it got
if len(sys.argv) == 3:
    # recive the params from bat - the path to find str in and the str to find
    param_path = sys.argv[1]
    param_str_to_find = sys.argv[2]

    # checks if the path exists
    if os.path.exists(param_path):
        with open(param_path, "r") as file:
            all_lines = file.readlines()
        for i in range(len(all_lines)):
            if param_str_to_find in all_lines[i]:
                print(str(i+1) + " " + all_lines[i])


    else:
        print("couldn't find file")

