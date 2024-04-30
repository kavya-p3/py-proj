from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions



class LoginPage:
    def __init__(self, dr):
        self.dr = dr


    username = (By.NAME, "TextField")
    password = (By.NAME, "password")
    loginbutton = (By.XPATH, "//span[text()='Login']")

    validation_message = (By.XPATH,'//p[text()="Incorrect user name or password. The maximum retry attempts allowed for login are 3. Your account will be locked for 30 minutes if you exceed 3 attempts."]')

    def enterUsername(self, username):
        wait2 = wait.WebDriverWait(self.dr, 15)
        wait2.until(expected_conditions.presence_of_element_located((LoginPage.username)))
        self.dr.find_element(*LoginPage.username).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.dr.find_element(*LoginPage.username).send_keys(username)

    def enterPassword(self,password):
        wait1 = wait.WebDriverWait(self.dr, 10)
        wait1.until(expected_conditions.presence_of_element_located((LoginPage.password)))
        self.dr.find_element(*LoginPage.password).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.dr.find_element(*LoginPage.password).send_keys(password)



    def clickLogin(self):
        self.dr.find_element(*LoginPage.loginbutton).click()






    def verifyValidationMessage(self):
        wait2 = wait.WebDriverWait(self.dr, 15)
        wait2.until(expected_conditions.presence_of_element_located((LoginPage.validation_message)))
        element = self.dr.find_element(*LoginPage.validation_message)
        return element






    # def loginwithcurrectcredentials(self):
    #
    #     wait2 = wait.WebDriverWait(self.dr, 15)
    #     wait2.until(expected_conditions.presence_of_element_located((LoginPage.username)))
    #     self.dr.find_element(*LoginPage.username).send_keys(LoginPage.data.cred[self.reg + 'username'])
    #     if self.reg == 'aan':
    #         self.dr.find_element(*LoginPage.continuebutton).click()
    #     wait1 = wait.WebDriverWait(self.dr, 10)
    #     wait1.until(expected_conditions.presence_of_element_located((LoginPage.password)))
    #     self.dr.find_element(*LoginPage.password).send_keys(LoginPage.data.cred[self.reg + 'password'])
    #
    #     self.dr.get_screenshot_as_file(self.filelocation+'Login.png')
    #     self.dr.find_element(*LoginPage.loginbutton).click()
    #     orgObject = OrganizationPage(self.dr,self.reg,self.filelocation)
    #     return orgObject
    #
    # def clickRegisterNewUserLink(self):
    #     wait2 = wait.WebDriverWait(self.dr, 15)
    #     if self.reg == 'aan':
    #         wait2.until(expected_conditions.presence_of_element_located((LoginPage.aan_nonmember_link)))
    #         self.dr.find_element(*LoginPage.aan_nonmember_link).click()
    #     else:
    #         wait2.until(expected_conditions.presence_of_element_located((LoginPage.register_here_link)))
    #         self.dr.find_element(*LoginPage.register_here_link).click()
    #     regObj = RegistrationPage(self.dr)
    #
    #     return regObj


