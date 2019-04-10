#changelog: uploads the files to the server via ftp


from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import ftplib
import os



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

#sends the file to server
def upload():
    print ("connecting")
    #ftp connection (server, user,pass)
    ftp = ftplib.FTP('mrcmrc.ddns.net','pi','esteesuntimelapsemuylargo')

    #folder from which to upload
    template_dir = '/home/pi/captures/'

    print ("uploading")
    #iterate through dirs and files 
    for root, dirs, files in os.walk(template_dir, topdown=True):
        relative = root[len(template_dir):].lstrip(os.sep)
       #enters dirs 
        for d in dirs:
            ftp.mkd(os.path.join(relative, d))
        #uploads files
        for f in files:
            ftp.cwd(relative)
            ftp.storbinary('STOR ' + f, open(os.path.join(template_dir, relative, f), 'rb'))
            ftp.cwd('/')

    ftp.quit()

    print ('all files have been uploaded successfully')



while True:
    #get date and time at eac iteration of the loop
    shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    captureImages()
    print ("downloading from camera")
    renameFiles(picID)
    upload()
    
   

#check the cron function to trigger shots at specific times 
                
    
