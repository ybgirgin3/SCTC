import os
import sys
import subprocess


# to make app run
# create config file
tbin = subprocess.check_output(['which', 'tesseract']).decode('utf-8').rstrip().strip()
with open("config.py", "w") as f:
    f.write(f"tess_path = '{tbin}'")

# to make app callable globally from terminal
# create exec file and move it
curPath = os.getcwd()
execFile = 'sctc' # SCreenToClipboard
binFolderPath = '/usr/local/bin'
pyBin = subprocess.check_output(['which', 'python3']).decode('utf-8').rstrip().strip()

# create exec file
with open(execFile, 'w') as f:
    ret = f"{pyBin} {os.path.join(curPath, 'getSS.py')}"
    f.write(ret)



# this part requires root previlege
# src -> dst
#subprocess.Popen(['sudo', 'mv', 'sctc', '/usr/local/bin'])
os.system("chmod +x sctc && sudo mv sctc /usr/local/bin")

