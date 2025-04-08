# -*- coding: utf-8 -*-
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
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://migrate.erp.quatrixglobal.com/web/login")
        email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))
        email.click()
        email.clear()
        email.send_keys("kelvin.kiarie@quatrixglobal.com")
        time.sleep(2)
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
        password.click()
        password.clear()
        password.send_keys("$kingara120")
        submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-primary') and contains(text(), 'Log in')]")))
        submit.click()
        
        menu = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='full' and @data-toggle='dropdown' and @data-display='static' and @accesskey='h']")))
        menu.click()

        dispatch_icon_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-menu-xmlid='quatrix_dispatch_module.dispatch_menu']")))
        dispatch_icon_btn.click()

        time.sleep(2)

        self.group_dispatch_quotes()
        
        self.open_dispatch_quote()

        self.complete_delivery()
        
        time.sleep(10)

    def group_dispatch_quotes(self):
        driver = self.driver
        group_by = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(@class, 'o_dropdown_toggler_btn')]//span[@class='o_dropdown_title' and text()='Group By']")))
        group_by.click()
        time.sleep(1)
        status = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-checked='false' and @role='menuitemcheckbox' and text()='Status']")))
        status.click()
        time.sleep(1)

    def open_dispatch_quote(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//th[@class='o_group_name' and contains(., 'Quotation')]"))).click()
        element = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='DO9357'])[1]/following::td[1]")))
        element.click()
        time.sleep(5)

    def complete_delivery(self):
        driver = self.driver
        complete_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "action_confirm")))
        complete_btn.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located)

    
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