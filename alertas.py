from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=1920,1080")  

driver = webdriver.Chrome(options=chrome_options)


wait = WebDriverWait(driver, 10)


driver.get("https://demoqa.com/alerts")



boton_confirmacion = wait.until(EC.element_to_be_clickable((By.ID, "confirmButton")))
boton_confirmacion.click()

alerta_confirmacion = wait.until(EC.alert_is_present())
print(f"Texto de la alerta de confirmación: {alerta_confirmacion.text}")
alerta_confirmacion.accept()

resultado_confirmacion = wait.until(EC.presence_of_element_located((By.ID, "confirmResult"))).text
print(f"Resultado después de aceptar la alerta: {resultado_confirmacion}")



boton_prompt = wait.until(EC.element_to_be_clickable((By.ID, "promtButton")))
boton_prompt.click()

alerta_prompt = wait.until(EC.alert_is_present())
texto_prompt = "¡El sistema dijo sí! Has aprobado todas las pruebas"
print(f"Texto enviado al prompt: {texto_prompt}")
alerta_prompt.send_keys(texto_prompt)
alerta_prompt.accept()

resultado_prompt = wait.until(EC.presence_of_element_located((By.ID, "promptResult"))).text
print(f"Resultado después de aceptar el prompt: {resultado_prompt}")


driver.quit()
