import subprocess
import os



commands = ["ls", "hexdump", "grep", "exit"]
#the command gives full path of where the file is saved
#so we can show it on screen and it can be recognized no matter where it is saved
full_path = os.path.dirname(os.path.abspath(__file__))
current_path = os.path.dirname(os.path.abspath(__file__))

while True:
    command = input(current_path + ">>>")

    if command == "hello":
        print(os.getlogin())
    elif command.split(" ")[0] == "cd":
        ####################need to check valid input
        #change folder
        current_path = command.split(" ")[1]
        os.chdir(current_path)
    elif command in commands:
        #run bat file
        # shell = True so we can run the command through the Windows shell in order to run the bat file
        subprocess.call(os.path.join(full_path, command), shell=True)
    else:
        pass
