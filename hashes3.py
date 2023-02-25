import hashlib
import os
import csv

folder_path = "D:/Votaciones 2023/HASHES CPCCS"
files = os.listdir(folder_path)
with open('D:/Votaciones 2023/HASHES CPCCS 2/hashes1.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
       
        md5 = hashlib.md5()
        md5.update(open(file_path, 'rb').read())
        md5_hash = md5.hexdigest()
       
        sha1 = hashlib.sha1()
        sha1.update(open(file_path, 'rb').read())
        sha1_hash = sha1.hexdigest()
       
        sha256 = hashlib.sha256()
        sha256.update(open(file_path, 'rb').read())
        sha256_hash = sha256.hexdigest()
       
        writer.writerow([file_name, md5_hash, sha1_hash, sha256_hash])