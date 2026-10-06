import subprocess
import os



commands = ["ls", "hexdump", "grep", "exit"]
#the command gives full path of where the file is saved
#so we can show it on screen and it can be recognized no matter where it is saved
full_path = os.path.dirname(os.path.abspath(__file__))

while True:
    command = input(full_path + ">>>")

    if command == "hello":
        print(os.getlogin())
    elif command == "cd":
        pass
    elif command in commands:
        #run bat file
        subprocess.call(os.path.join(full_path, command), shell=True)
    else:
        pass
