import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def calcular_frete_jadlog(origem, destino, peso):
    try:
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        service = Service(r"C:\Users\LorrayneBentoPinheir\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()  # Maximiza a janela

        driver.get("https://www.jadlog.com.br/jadlog/home")
        wait = WebDriverWait(driver, 20)
        time.sleep(3)  # Aguarde a página carregar

        # Fechar pop-up de alerta (X no canto superior direito)
        try:
            close_alert = driver.find_element(By.CSS_SELECTOR, "div.swal2-popup button.swal2-close")
            close_alert.click()
            print("Pop-up de alerta fechado.")
            time.sleep(1)
        except Exception:
            print("Pop-up de alerta não encontrado.")

        # Fechar pop-up de cookies
        try:
            close_cookies = driver.find_element(By.XPATH, "//button[contains(text(),'Aceitar todos os cookies')]")
            close_cookies.click()
            print("Pop-up de cookies fechado.")
            time.sleep(1)
        except Exception:
            print("Pop-up de cookies não encontrado.")

        origem_input = driver.find_element(By.ID, "cepOrigem")
        destino_input = driver.find_element(By.ID, "cepDestino")
        peso_input = driver.find_element(By.ID, "peso")
        btn_calcular = driver.find_element(By.ID, "btnCalcular")

        origem_input.send_keys(origem)
        destino_input.send_keys(destino)
        peso_input.send_keys(str(peso))
        btn_calcular.click()

        print("Campos preenchidos e botão clicado.")

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
        driver.quit()
        return {"erro": f"Erro ao calcular frete: {str(e)}"}