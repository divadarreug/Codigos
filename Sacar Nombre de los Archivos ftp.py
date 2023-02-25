import ftplib
import csv

ftp = ftplib.FTP("ftp.vecinosenaccion-riobamba.com")
ftp.login("u213299148.soporte", "$23Riobamba2E*")
ftp.cwd("/junta_alcalde_0601")

files = ftp.nlst()

with open('filenames.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Filename'])
    for filename in files:
        writer.writerow([filename])

ftp.quit()