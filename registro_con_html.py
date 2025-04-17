import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_html_report(result):
    html_content = f"""
    <html>
    <head><title>Resultado de la prueba de formulario</title></head>
    <body>
        <h1>Resultado de la prueba de formulario</h1>
        <p>{result}</p>
    </body>
    </html>
    """

    with open("resultado_formulario.html", "w") as file:
        file.write(html_content)


def test_form_submission():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://demoqa.com/automation-practice-form")

   
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )

    
    driver.find_element(By.ID, "firstName").send_keys("Dafne")
    driver.find_element(By.ID, "lastName").send_keys("Cortes")
    driver.find_element(By.ID, "userEmail").send_keys("dafne.cortes@example.com")
    driver.find_element(By.XPATH, '//label[text()="Female"]').click()
    driver.find_element(By.ID, "userNumber").send_keys("3001234567")

   
    driver.execute_script("window.scrollBy(0, 300)")
    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    driver.execute_script("arguments[0].click();", submit_btn)

   
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    mensaje = driver.find_element(By.ID, "example-modal-sizes-title-lg").text

   
    if "Thanks for submitting the form" in mensaje:
        result = " El formulario se ha enviado exitosamente."
    else:
        result = " Falló el envío del formulario"

    
    create_html_report(result)

    driver.quit()


test_form_submission()
