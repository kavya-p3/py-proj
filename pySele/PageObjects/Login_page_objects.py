from selenium.webdriver.common.by import By


class LoginObj():
    def __init__(self, dr):
        self.dr = dr

    username = (By.NAME, "TextField")
    password = (By.NAME, "password")
    loginButton = (By.XPATH, "//span[text()='Login']")

    def getUsername(self):
        return self.dr.find_element(*LoginObj.username)

    def getPassword(self):
        return self.dr.find_element(*LoginObj.password)

    def getLoginButton(self):

        return self.dr.find_element(*LoginObj.loginButton)




