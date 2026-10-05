import subprocess
import os


#the command gives full path - so it can be recognised no matter where it is saved
full_path = os.path.dirname(os.path.abspath(__file__))

#run bat file
subprocess.call(os.path.join(full_path, "ls.bat"), shell=True)