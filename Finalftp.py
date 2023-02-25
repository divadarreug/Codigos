import ftplib
import requests

ftp = ftplib.FTP("ftp.vecinosenaccion-riobamba.com")
ftp.login("u213299148.soporte", "$23Riobamba2E*")
ftp.cwd("/junta_alcalde_0601")

files = ftp.nlst()
for file in files:
    with open("." + file, 'wb') as f:
        ftp.retrbinary("RETR " + file, f.write)
    files = {'file': open("." + file, 'rb')}
    requests.post("http://localhost:8081/upload", files=files, data={'filename': file})

ftp.quit()