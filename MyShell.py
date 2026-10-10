import subprocess
import os
import sys




commands = ["ls", "hexdump", "grep"]
#the command gives full path of where the file is saved
#so we can show it on screen and it can be recognized no matter where it is saved
full_path = os.path.dirname(os.path.abspath(__file__))

while True:
    # os.getcwd() = gives the path that the program runs in right now
    command = input(os.getcwd() + ">>>")
    splitted_command = command.split(" ")
    if splitted_command[0] == "exit":
        break
    elif splitted_command[0].lower() == "hello":
        print(os.getlogin())
    elif splitted_command[0] == "cd":
        #cd and then path or .. or \
        if len(splitted_command) == 2:
            if splitted_command[1] != ".." and splitted_command[1] != "\\":
                # checks if the path exists and if it is a folder(directory)
                if os.path.isdir(splitted_command[1]):
                    #change folder
                    os.chdir(splitted_command[1])
                else:
                    print("not legall path")
            else:
                #change folder
                os.chdir(splitted_command[1])
        else:
            print("needs exactly 1 param (path or .. or /)")

    elif splitted_command[0] in commands:
        #put the batch path in place 0 instead of the command itself so it know which file to go to
        splitted_command[0] = os.path.join(full_path, splitted_command[0]) + ".bat"
        # run bat file
        # shell = True so we can run the command through the Windows shell in order to run the bat file
        subprocess.call(splitted_command, shell=True)

    else:
        pass

sys.exit()

