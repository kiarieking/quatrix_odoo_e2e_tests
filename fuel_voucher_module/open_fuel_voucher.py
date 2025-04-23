from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        options = Options()
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444', options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://migrate.erp.quatrixglobal.com/web/login")
        time.sleep(2)
        email=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "login")))
        email.clear()
        email.send_keys("kelvin.kiarie@quatrixglobal.com")
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
        password.clear()
        password.send_keys("$kingara120")
        submit_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_btn.click()
        i_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i")))
        i_element.click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
