from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


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


def create_html_report(confirm_result, prompt_result):
    html_content = f"""
    <html>
    <head>
        <title>Informe de Alertas</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            h1 {{
                color: #333;
            }}
            .result {{
                margin-top: 20px;
                padding: 10px;
                border: 1px solid #ddd;
            }}
            .success {{
                background-color: #d4edda;
                color: #155724;
            }}
            .error {{
                background-color: #f8d7da;
                color: #721c24;
            }}
        </style>
    </head>
    <body>
        <h1>Informe de Interacción con las Alertas</h1>
        <div class="result success">
            <h2>Resultado de la Alerta de Confirmación</h2>
            <p>{confirm_result}</p>
        </div>
        <div class="result success">
            <h2>Resultado del Prompt</h2>
            <p>{prompt_result}</p>
        </div>
    </body>
    </html>
    """
    
    
    with open("informe_alertas.html", "w") as file:
        file.write(html_content)
    print("Informe HTML generado exitosamente.")


create_html_report(resultado_confirmacion, resultado_prompt)

driver.quit()
