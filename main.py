from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

navegador = webdriver.Chrome()

navegador.get('https://www.tripadvisor.com.br/')
time.sleep(6)
navegador.find_element("xpath",'//*[@id="onetrust-accept-btn-handler"]').click()
time.sleep(6)
navegador.find_element("xpath",'//*[@id="lithium-root"]/main/div[3]/div/div/div[2]/form/input[1]').send_keys('Congresso Nacional - Brasília')
time.sleep(6)
navegador.find_element("xpath",'//*[@id="typeahead_results"]/a[1]').click()
time.sleep(6)
num_avaliacao = navegador.find_element("xpath",'//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[1]/div[2]/span').text
avaliacao = navegador.find_element("xpath",'//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[1]/div[1]').text
time.sleep(6)
print("\n## Resultado da coleta de dados ##","\nAvaliação do local:", avaliacao, 'de', num_avaliacao +'.\n')
navegador.close()
