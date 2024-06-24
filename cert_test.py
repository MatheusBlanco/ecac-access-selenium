import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.headless = False
EC = driver.get("https://cav.receita.fazenda.gov.br/autenticacao/login")
print('\n\nEC: ',EC)
wait = WebDriverWait(driver, 30)

driver.find_element(By.XPATH, '//*[@id="login-dados-certificado"]/p[2]/input').click()
driver.implicitly_wait(3)

# print('antes de pegar o cert button\n\n\n')
# driver.find_element(By.XPATH,'//*[@class="item-login-signup-ways"]/a').click()
# print('\n\ndepois de pegar o cert button')
# wait.until(EC.alert_is_present())
# driver.switch_to.alert.accept()

time.sleep(10)