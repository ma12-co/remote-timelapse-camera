#changelog: files actually do rename now


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



#The title of the project goes here, put a space after the name
picID = "WithFor"

#define function that calls the gphoto2 command
triggerCommand = ["--capture-image-and-download"]
def captureImages():
    gp(triggerCommand)

#Rename the files in order to display project name,
#date and time in each capture
def renameFiles (ID):
    for filename in os.listdir("."):
        if len(filename) < 13:
            if filename.endswith (".jpg"):
                os.rename (filename, ( ID + shot_time + ".jpg"))
                print ("jpg renamed")
            elif filename.endswith(".arw"):
                os.rename (filename, ( ID + shot_time + ".arw"))
                print ("arw renamed")


while True:
    killgphoto2Process()
    #get date and time at eac iteration of the loop
    shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    captureImages()
    renameFiles(picID)


#check the cron function to trigger shots at specific times 
                
    
