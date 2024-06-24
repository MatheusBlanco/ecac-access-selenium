import time

import pyautogui
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

# Initialize web browser with Chrome options
driver = uc.Chrome(options=chrome_options)

# Acesse o eCAC
url = "https://cav.receita.fazenda.gov.br/ecac/"
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="login-dados-certificado"]/p[2]/input').click()
wait = WebDriverWait(driver, 10)

cert_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-certificate"]')))

cert_button.click()

services_menu_is_visible = wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="menu-servicos"]'), 'Contribuinte,'))
groups_list = driver.find_element(By.XPATH, '//*[@id="grupos"]')
options = groups_list.find_elements(By.CSS_SELECTOR, 'li')

for option in options:
  if (option.text == 'Certidões e Situação Fiscal'):
    option.click()

fiscal_situation_options = driver.find_element(By.XPATH, '//*[@id="containerServicos271"]/div/ul')

fiscal_situation_buttons = driver.find_element(By.XPATH, '//*[@id="containerServicos271"]/div/ul/li[1]/a')
fiscal_situation_buttons.click()

time.sleep(5)

cadin_iframe = driver.find_element(By.XPATH, '//*[@id="frmApp"]')

driver.switch_to.frame(cadin_iframe)

cadin_header = driver.find_element(By.CLASS_NAME, 'srfb-page-title')
print(cadin_header.text)

cnpj = driver.find_element(By.ID, 'cnpjCpf')
print(cnpj.text)

time.sleep(1)
driver.switch_to.default_content()
driver.find_element(By.XPATH, '//*[@id="sairSeguranca"]').click()
driver.quit()
