import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

def calcular_frete_jadlog(origem, destino, peso):
    driver = None
    try:
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        service = Service(r"C:\Users\LorrayneBentoPinheir\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

        driver.get("https://www.jadlog.com.br/jadlog/simulacao")
        wait = WebDriverWait(driver, 20)

        # Fechar pop-up de alerta (clicando fora da janela)
        try:
            modal = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modalHome"]')))
            actions = ActionChains(driver)
            actions.move_to_element_with_offset(modal, -50, -50).click().perform()
            print("Pop-up de alerta fechado (clic fora da janela).")
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

        # Aguarda os campos aparecerem usando os novos XPaths/IDs
        origem_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="origem"]')))
        destino_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="destino"]')))
        peso_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="peso"]')))
        btn_calcular = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form_precifica"]/div[3]/div[4]/div/input')))

        origem_input.send_keys(origem)
        destino_input.send_keys(destino)
        peso_input.send_keys(str(peso))
        btn_calcular.click()

        print("Campos preenchidos e botão clicado.")

        # Aguarda o resultado aparecer (ajuste o seletor conforme necessário)
        resultado = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "valor-total"))).text
        prazo = driver.find_element(By.CLASS_NAME, "prazo-entrega").text

        time.sleep(3)  # Mantém a janela aberta por mais tempo para visualização

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
        if driver:
            driver.quit()
        return {"erro": f"Erro ao calcular frete: {str(e)}"}