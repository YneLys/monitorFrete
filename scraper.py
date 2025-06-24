from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def calcular_frete_jadlog(origem, destino, peso):
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)

        driver.get("https://www.jadlog.com.br/jadlog/home")
        wait = WebDriverWait(driver, 20)

        wait.until(EC.presence_of_element_located((By.ID, "cepOrigem"))).send_keys("01001-000")
        driver.find_element(By.ID, "cepDestino").send_keys("20040-000")
        driver.find_element(By.ID, "peso").send_keys(str(peso))

        driver.find_element(By.ID, "btnCalcular").click()

        resultado = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "valor-total"))).text
        prazo = driver.find_element(By.CLASS_NAME, "prazo-entrega").text

        driver.quit()

        return {
            "transportadora": "Jadlog",
            "valor_frete": resultado,
            "prazo_estimado": prazo
        }

    except Exception as e:
        return {"erro": f"Erro ao calcular frete: {str(e)}"}