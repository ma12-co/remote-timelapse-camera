from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

#kill gphoto2process that
#starts whenever we connect the
#camera

def killgphoto2Process ():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate ()

    # Search for the line that has the process
    #we want to kill
    for line in out.splitlines ():
        if b'gvfs-gphoto2-vo' in line:
            #kill the process!
            pid = int(line.split (None, 1) [0])
            os.kill(pid, signal.SIGKILL)

shot_date = datetime.now() .strftime("%Y-%m-%d")
shot_time = datetime.now() .strftime("%Y-%m-%d %H:%M:%S")
picID = "PiShots"

triggerCommand = ["--capture-image-and-download"]

folder_name = shot_date + picID
save_location = "/home/captures" + folder_name


def captureImages():
    gp(triggerCommand)


def renameFiles (ID):
    for filename in os.listdir("."):
        if len(filename) < 13:
            if filename.endswith (".jpg"):
                os.rename (filename, (shot_time + ID + ".jpg"))
                print ("jpg renamed")
            elif filename.endswith(".arw"):
                os.rename (filename, (shot_time + ID + ".arw"))
                print ("arw renamed")


while True:
    killgphoto2Process()
    captureImages()
    renameFiles(picID)
                
    
