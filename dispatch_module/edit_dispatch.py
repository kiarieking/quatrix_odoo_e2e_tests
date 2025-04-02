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
        driver.get("https://migrate.erp.quatrixglobal.com/web/login")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("$kingara120")
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("kelvin.kiarie@quatrixglobal.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//i").click()
        driver.find_element_by_xpath("//img[contains(@src,'data:image/png;base64,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QhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACxEAQAAwEIUAAAALEQBAADAQhQAAAAsRAEAAMBCFAAAACz0/wEbBPjfGiI9ngAAAABJRU5ErkJggg==')]").click()

        time.sleep(10)
        
        self.group_dispatch_quotes()
       
        self.open_dispatch_quote()

        self.click_edit_btn()

        self.edit_customer()

        self.edit_vehicle_registration()

        self.edit_dispatch_date()

        # self.edit_delivery_date()

        # self.add_product_line()

        self.save_changes()

    def group_dispatch_quotes(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(@class, 'o_dropdown_toggler_btn')]//span[@class='o_dropdown_title' and text()='Group By']"))).click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@aria-checked='false' and @role='menuitemcheckbox' and text()='Status']").click()
        time.sleep(1)

    def open_dispatch_quote(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//th[@class='o_group_name' and contains(., 'Quotation')]"))).click()
        element = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='DO9357'])[1]/following::td[1]")))
        element.click()
        time.sleep(5)

    def click_edit_btn(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'o_form_button_edit')]//span[text()='Edit']"))).click()

    def edit_customer(self):
        driver = self.driver
        customer_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME,"partner_id")))
        customer_input.click()
        search_more = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='o_m2o_dropdown_option ui-menu-item']/a[text()='Search More...']")))
        search_more.click()
        new_customer = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//tr[@class='o_data_row' and @data-id='res.partner_13']/td[contains(text(), 'ALEX OGONDA')]")))
        new_customer.click()
        time.sleep(5)

    def edit_vehicle_registration(self):
        driver = self.driver
        vehicle_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME,"vehicle_id")))
        vehicle_input.click()
        search_more = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='o_m2o_dropdown_option ui-menu-item']/a[text()='Search More...']")))
        search_more.click()
        new_vehicle = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//tr[td[@title='KAA015K']]//td//span[text()='Mitsubishi/Mitsubishi']")))
        new_vehicle.click()
        time.sleep(5)

    def edit_dispatch_date(self):
        driver = self.driver
        dispatch_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "date_dispatch")))
        dispatch_date.click()
        specific_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//td[text()="4"]')))
        specific_date.click()
        time.sleep(5)

    def edit_delivery_date(self):
        driver = self.driver
        delivery_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "date_delivery")))
        delivery_date.click()
        specific_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//td[text()="6"]')))
        specific_date.click()
        time.sleep(5)

    def add_product_line(self):
        driver = self.driver
        add_line = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//td[@class='o_field_x2many_list_row_add']/a[text()='Add a line']")))
        add_line.click()
        product_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='o_input_dropdown']/input")))
        product_input.send_keys("[HACO] Embakasi-Updated MERU 7T")
        time.sleep(5)



    def save_changes(self):
        driver = self.driver
        save_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary o_form_button_save' and span[text()='Save']]")))
        save_btn.click()

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
