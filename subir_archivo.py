from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import glob


ruta_descarga = os.path.join(os.path.expanduser("~"), "Downloads")
os.makedirs(ruta_descarga, exist_ok=True)


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": ruta_descarga,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})


driver = webdriver.Chrome(options=chrome_options)


nombre_archivo = "pruebaFile.txt"
contenido = "archivo de prueba que se genera mediante el mismo código, espero que funcione"
carpeta_recursos = os.path.join(os.getcwd(), "recursos")
os.makedirs(carpeta_recursos, exist_ok=True)
ruta_archivo = os.path.join(carpeta_recursos, nombre_archivo)

with open(ruta_archivo, "w") as archivo:
    archivo.write(contenido)
print(f"Archivo generado exitosamente: {ruta_archivo}")


driver.get("https://demoqa.com/upload-download")
driver.find_element(By.ID, "uploadFile").send_keys(ruta_archivo)
time.sleep(3)

mensaje_archivo = driver.find_element(By.ID, "uploadedFilePath").text
if os.path.basename(ruta_archivo) in mensaje_archivo:
    print("El archivo se ha subido correctamente")
else:
    print("El archivo no se subió correctamente")


driver.get("https://demoqa.com/upload-download")
driver.find_element(By.ID, "downloadButton").click()
time.sleep(10)


archivos_descargados = glob.glob(os.path.join(ruta_descarga, "sampleFile*"))

if archivos_descargados:
    print(f"El archivo se ha descargado correctamente en: {ruta_descarga}")
else:
    print("El archivo no se descargó. Revisa si Chrome lo bloqueó o si hubo algún error.")

driver.quit()
