import time
import winreg

import undetected_chromedriver as uc
from cryptography.hazmat.primitives.serialization import pkcs12
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def UpdateStringValue(strigValueName, newValueOfStrinValue, stringValuePath):
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, stringValuePath, 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, strigValueName, 0, winreg.REG_SZ, newValueOfStrinValue)
    winreg.CloseKey(key)


def GetCertificate(pathOfCertificate, passwordOfCertifcate):
    # pkcs12 = crypto.load_pkcs12(open(pathOfCertificate, 'rb').read(), passwordOfCertifcate)
    with open(pathOfCertificate, "rb") as f:
        private_key, certificate, additional_certificates = pkcs12.load_key_and_certificates(f.read(), passwordOfCertifcate)
    # return pkcs12.get_certificate()
    return certificate


if __name__ == "__main__":
    # pathOfstringValue = 'SOFTWARE\Policies\Google\Chrome\AutoSelectCertificateForUrls'
    # stringValueName = '1'

    # certificate = GetCertificate(r"562- METODOLOGIA STARTUP LTDA.pfx", bytes("Rogerio123", 'UTF-8'))
    # print(certificate)
    # subject = certificate.subject
    # issuer = certificate.issuer

    # CN_subject = subject.rfc4514_string()
    # CN_subject_value = CN_subject.split(',')[0].split('=')[1]
    # C_suject_value = CN_subject.split(',')[-1].split('=')[1]
    # O_subject_value = CN_subject.split(',')[-2].split('=')[1]

    # CN_issuer = issuer.rfc4514_string()
    # CN_issuer_value = CN_issuer.split(',')[0].split('=')[1]
    # C_issuer_value = CN_issuer.split(',')[-1].split('=')[1]
    # O_issuer_value = CN_issuer.split(',')[-2].split('=')[1]

    # url_where_certificate_will_be_send = "https://certificado.sso.acesso.gov.br/"
    # json = '{"pattern":"' + url_where_certificate_will_be_send + '","filter":{"ISSUER":{"CN":"' + CN_issuer_value + '","C":"' + C_issuer_value + '","O":"' + O_issuer_value + '"},"SUBJECT":{"CN":"' + CN_subject_value + '","C":"' + C_suject_value + '","O":"' + O_subject_value + '"}}}'
    # print(json)

    # UpdateStringValue(stringValueName, json, pathOfstringValue)

    url = 'https://cav.receita.fazenda.gov.br/autenticacao/login'
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")

    driver = uc.Chrome()
    print('Iniciando Chrome')
    driver.get(url)
    print('Acessando Pagina')
    driver.find_element(By.XPATH, '//*[@id="login-dados-certificado"]/p[2]/input').click()
    wait = WebDriverWait(driver, 10)

    cert_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-certificate"]')))

    cert_button.click()
    print('\n\nCert button: ', cert_button, '\n\n')

    time.sleep(1000)

    driver.quit()
