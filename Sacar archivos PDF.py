import os
import shutil

def copy_pdf_files(src_folder, dst_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.endswith(".pdf"):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_folder, file)
                shutil.copy2(src_file, dst_file)

src_folder = "D:/Votaciones 2023/Hashes/CPCCS/IMG_ACTAS/16-CPCCS (MUJERES)"
dst_folder = "D:/Votaciones 2023/Prueba"
copy_pdf_files(src_folder, dst_folder)