import os
import sys
import shutil

# this part requires root previlege
# src -> dst
def sudopart():
    if os.geteuid () == 0:
        shutil.move(os.path.join(curPath, execFile), os.path.join(binFolderPath, execFile))
        print("installation done")
    else: sys.exit("We need to root permissions to move file to '/usr/local/bin'.. so please run file with sudo 🤕")

if __name__ == '__main__':
    sudopart()
