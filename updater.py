import os
import subprocess
import sys
import time

subprocess.run(["winget", "update"])
input("Press Enter to continue with the upgrade...")
subprocess.run(["winget", "upgrade", "--all"])

os.system(input("Press Enter to continue with the cleanup..."))
os.system("winget cleanup") 
