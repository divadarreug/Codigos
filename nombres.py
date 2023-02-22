import os
import pandas as pd

ruta_carpeta = r"\\172.20.136.226\Respaldos\2022"

nombres_archivos = os.listdir(ruta_carpeta)


df_archivos = pd.DataFrame(nombres_archivos, columns=["Nombre del archivo"])


nombre_archivo_excel = "lista_archivos_2022.xlsx"
df_archivos.to_excel(nombre_archivo_excel, index=False)