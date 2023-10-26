from selenium import webdriver
from selenium.webdriver.common.by import By
import time, logging

from config import *
from secret import USER, PASSWORD

class SeleniumScrapperPepal:

    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        
        if HEADLESS:
            options.add_argument('--headless')
            
        self.driver = webdriver.Chrome(options=options)

    def connectionPepal(self):
        self.driver.get(PEPAL_URL)

        emailField = self.driver.find_element(By.ID, "username")
        passwordField = self.driver.find_element(By.ID, "password")

        emailField.send_keys(USER)
        passwordField.send_keys(PASSWORD)

        self.driver.find_element(By.ID, "login_btn").click()
        time.sleep(0.5)

    def validePresence(self):
        self.driver.get(PRESENCE)

        btn = self.driver.find_element(By.XPATH, '//*[@id="body_presences"]/tr[@class="warning"]/td[3]/a')
        
        if btn.text == "Relevé de présence":
            print(btn)
            time.sleep(3)
            
            try:
                close = self.driver.find_element(By.XPATH, '//*[@id="body_presences"]/tr[1]/td[4]/div/span[@class="text-danger"]')
                
                if close.text == "L'appel est clôturé.":
                    logging.warning("Appel cloturé")
                    
            except:
                self.driver.get(btn.get_attribute("href"))

                try:
                    self.driver.find_element(By.ID, "set-presence").click()
                    logging.info("Appel validé !")
                    
                except:
                    logging.error("Pas de bouton pour valider la presence")

    def run(self):
        self.connectionPepal()
        self.validePresence()

        self.driver.close()
