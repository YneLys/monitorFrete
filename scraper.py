from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # Adicione esta linha

def calcular_frete_jadlog(origem, destino, peso):
    try:
        options = Options()
        #options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        service = Service(r"C:\Users\LorrayneBentoPinheir\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")  # Use Service

        driver = webdriver.Chrome(service=service, options=options)  # Corrija aqui

        driver.get("https://www.jadlog.com.br/jadlog/home")
        wait = WebDriverWait(driver, 20)

        wait.until(EC.presence_of_element_located((By.ID, "cepOrigem"))).send_keys(origem)
        driver.find_element(By.ID, "cepDestino").send_keys(destino)
        driver.find_element(By.ID, "peso").send_keys(str(peso))

        driver.find_element(By.ID, "btnCalcular").click()

        resultado = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "valor-total"))).text
        prazo = driver.find_element(By.CLASS_NAME, "prazo-entrega").text

        driver.quit()

        return {
            "transportadora": "Jadlog",
            "cep_origem": origem,
            "cep_destino": destino,
            "peso": peso,
            "valor_frete": resultado,
            "prazo_estimado": prazo
        }

    except Exception as e:
        return {"erro": f"Erro ao calcular frete: {str(e)}"}