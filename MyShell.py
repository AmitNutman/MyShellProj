#https://github.com/AmitNutman/MyShellProj

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
    elif splitted_command[0] == "?":
        # write the output of the command to the file
        if ">" in splitted_command:
            # the file path to write into is in the last index of list
            with open(splitted_command[-1], "w") as file_to_write_into:
                file_to_write_into.write("exit\nhello\ncd\nls\ngrep\nhexdump")
        else:
            print("exit\nhello\ncd\nls\ngrep\nhexdump")
    elif splitted_command[0].lower() == "hello":
        # write the output of the command to the file
        if ">" in splitted_command:
            # the file path to write into is in the last index of list
            with open(splitted_command[-1], "w") as file_to_write_into:
                file_to_write_into.write("hello " + os.getlogin())
        else:
            print("hello " + os.getlogin())
    elif splitted_command[0] == "cd":
        #cd and then path or .. or \
        if len(splitted_command) == 2:
            if splitted_command[1] != ".." and splitted_command[1] != "\\":
                # checks if the path exists and if it is a folder(directory)
                if os.path.isdir(splitted_command[1]):
                    #change folder
                    os.chdir(splitted_command[1])
                else:
                    print("not legal path")
            else:
                #change folder
                os.chdir(splitted_command[1])
        else:
            print("needs exactly 1 param (path or .. or /)")

    elif splitted_command[0] in commands:
        #put the batch path in place 0 instead of the command itself so it know which file to go to
        splitted_command[0] = os.path.join(full_path, splitted_command[0]) + ".bat"
        if "|" in splitted_command:
            command_pipe = command.split("|")
            #without the last char - space before |
            first_command = command_pipe[0][:-1].split(" ")
            #withut the first char - space after |
            second_command = command_pipe[1][1:].split(" ")
            first_command[0] = os.path.join(full_path, first_command[0]) + ".bat"
            second_command[0] = os.path.join(full_path, second_command[0]) + ".bat"
            #run the first command and save the result in pipe
            first = subprocess.Popen(first_command, stdout=subprocess.PIPE, shell = True)
            #run the second command with the first command output
            second = subprocess.Popen(second_command, stdin=first.stdout, stdout=None, shell=True)
            first.stdout.close()
            second.communicate()
        elif ">" in splitted_command:
            # write the output of the command to the file
            #the file path to write into is in the last index of list
            with open(splitted_command[-1], "w") as file_to_write_into:
                #call the bat file without the last 2 params(> and file to write into)
                # stdout=file_to_write_into - instead of printing the output, write in into the file
                subprocess.call(splitted_command[:-2], stdout=file_to_write_into, shell=True)
        else:
            # run bat file
            # shell = True so we can run the command through the Windows shell in order to run the bat file
            subprocess.call(splitted_command, shell=True)
    else:
        print("not legal command")

sys.exit()

