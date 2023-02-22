import os
import pandas as pd

ruta_carpeta = r"\\172.XXX.XXX.XXX\" #(Nombre de la carpeta )

nombres_archivos = os.listdir(ruta_carpeta)


df_archivos = pd.DataFrame(nombres_archivos, columns=["Nombre del archivo"])


nombre_archivo_excel = "lista_archivos_2022.xlsx" #(Nombre del archivo excel)
df_archivos.to_excel(nombre_archivo_excel, index=False)
