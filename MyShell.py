import subprocess
import os



commands = ["ls", "hexdump", "grep", "exit"]
#the command gives full path of where the file is saved
#so we can show it on screen and it can be recognized no matter where it is saved
full_path = os.path.dirname(os.path.abspath(__file__))

while True:
    # os.getcwd() = gives the path that the program runs in right now
    command = input(os.getcwd() + ">>>")
    splitted_command = command.split(" ")

    if splitted_command[0] == "exit":
        break
    elif splitted_command[0] == "hello":
        print(os.getlogin())
    elif splitted_command[0] == "cd":
        ####################need to check valid input
        #change folder
        os.chdir(command.split(" ")[1])
    elif splitted_command[0] in commands:
        #put the batch path in place 0 instead of the command itself so it know which file to go to
        splitted_command[0] = os.path.join(full_path, splitted_command[0]) + ".bat"
        # run bat file
        # shell = True so we can run the command through the Windows shell in order to run the bat file
        subprocess.call(splitted_command, shell=True)

    else:
        pass
