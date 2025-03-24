# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
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
        driver.get("http://migrate.erp.quatrixglobal.com:8069/web/login")
        driver.find_element_by_id("login").click()
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("kelvin.kiarie@quatrixglobal.com")
        driver.find_element_by_xpath("//div[@id='wrapwrap']/main/div").click()
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("$kingara120")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Discuss'])[1]/preceding::a[1]").click()
        driver.find_element_by_xpath("//img[contains(@src,'data:image/png;base64,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')]").click()

        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Filters'])[1]/following::span[1]").click()
        # driver.find_element_by_link_text("Status").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancelled (24)'])[1]/following::th[2]").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CO11623'])[1]/following::td[2]").click()

        self.group_orders()

        self.open_order()

        self.click_edit_button()

        self.change_vehicle_registration()

        self.change_delivery_number()

        self.change_reference_number()

        self.change_description()

        self.change_quantity()

        self.change_cost()

        self.change_date()

    def confirm_changes(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "action_confirm")))
        element.click()
        time.sleep(3)

    def change_date(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "date")))
        element.click()
        time.sleep(1)
        element.clear()
        element.send_keys("08/01/2024 00:00:00")
        time.sleep(3)

    def change_quantity(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "quantity")))
        element.clear()
        element.send_keys("2")
        time.sleep(3)

    def change_cost(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "carrier_price")))
        element.clear()
        element.send_keys("100000")
        time.sleep(3)


    def change_description(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "description")))
        element.clear()
        element.send_keys("KCJ389LZD5916:Kisumu")
        time.sleep(3)
        
    def change_reference_number(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "reference")))
        element.clear()
        element.send_keys("DO9429")
        time.sleep(3)

    def change_delivery_number(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "order_no")))
        element.clear()
        element.send_keys("632-IAT0001378")

    def change_vehicle_registration(self):
        driver = self.driver
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#o_field_input_905")))
        time.sleep(3)
        element.click()
        time.sleep(3)
        
        element1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ui-id-9")))
        time.sleep(3)
        element1.click()
        time.sleep(3)
        
        WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,"//tr[td[text()='KAA293B'] and td//span[text()='ramodas']]//span[text()='ramodas']"))).click()
        time.sleep(3)

    def group_orders(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//i[@class='fa fa-bars']/following-sibling::span[text()='Group By']"))).click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@aria-checked='false' and @role='menuitemcheckbox' and text()='Status']").click()
        time.sleep(1)
        

    def open_order(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//th[@class='o_group_name' and contains(., 'Quotation')]"))).click()
        element = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='CO11631'])[1]/following::td[1]")))
        element.click()
        time.sleep(2)

    def click_edit_button(self):
        driver = self.driver
        element = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".o_form_button_edit")))
        element.click()

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
