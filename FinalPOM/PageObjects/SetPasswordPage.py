from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SetPasswordPage:
    def __init__(self, dr):
        self.dr = dr

    password = (By.XPATH, '//input[@name="password"]')
    confirm_password = (By.XPATH, '//label[text()="Confirm Password"]/ancestor::div[@class="MuiFormControl-root input-field__container MuiFormControl-fullWidth"]/div/input')
    submit_button = (By.XPATH, '//span[text()="SUBMIT"]')
    success_msg = (By.XPATH,'//h6[text()="Password Created Successfully"]')

    def set_password(self,value):
        self.dr.find_element(*SetPasswordPage.password).send_keys(value)

    def set_confirm_password(self,value):
        self.dr.find_element(*SetPasswordPage.confirm_password).send_keys(value)

    def click_submit(self):
        self.dr.find_element(*SetPasswordPage.submit_button).click()