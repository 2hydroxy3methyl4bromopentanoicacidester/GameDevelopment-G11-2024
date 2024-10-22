import os
from selenium import webdriver

FEDAUTH = os.environ.get("FedAuth")

initialSamlURL = "https://sd75.onlinelearningbc.com/"

driver = webdriver.Chrome()

driver.get(initialSamlURL)
driver.add_cookie({"name": "FedAuth", "value": FEDAUTH})
driver.refresh()

try:
    while True:
        pass
except KeyboardInterrupt:
    driver.close()
    exit()