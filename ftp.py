import ftplib

# Open FTP session
session = ftplib.FTP('mrcmrc.ddns.net','pi','esteesuntimelapsemuylargo')
# file to send
file = open('marcovio.jpg','rb')                  
# send the file
session.storbinary('STOR '+'marcovio.jpg', file)     
# close file and FTP
file.close()                                    
session.quit()
