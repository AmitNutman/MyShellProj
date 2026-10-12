import sys
import os


#always has at least 1 param with file name(grep.py). the second and third param is what it got
#if got both file path and str to look for
if len(sys.argv) == 3:
    # recive the params from bat - the path to find str in and the str to find
    param_path = sys.argv[1]
    param_str_to_find = sys.argv[2]

    # checks if the path exists
    if os.path.exists(param_path):
        with open(param_path, "r") as file:
            content = file.readlines()
        for i in range(len(content)):
            if param_str_to_find in content[i]:
                print(str(i+1) + " " + content[i])

    else:
        print("couldn't find file")

#if got only str to look for
elif len(sys.argv) == 2:
    param_str_to_find = sys.argv[1]
    #the content to find str in
    content = sys.stdin.readlines()
    for i in range(len(content)):
        if param_str_to_find in content[i]:
            print(str(i + 1) + " " + content[i])

else:
    print("not legal amount of params - gets only path and str / pipe and then gets only str")


