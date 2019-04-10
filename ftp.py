#CHANGELOG: Uploads all files in the folder

import ftplib
import os


#ftp connection (server, user,pass)
ftp = ftplib.FTP('mrcmrc.ddns.net','pi','esteesuntimelapsemuylargo')

#folder from which to upload
template_dir = '/home/pi/ftp/files/'

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
