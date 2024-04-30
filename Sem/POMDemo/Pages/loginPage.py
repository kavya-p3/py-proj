class LoginPage():


    def __init__(self,dr):
        self.dri=dr
        self.username_textbox_id='txtUsername'
        self.password_textbox_id='txtPassword'
        self.submit_button_id='btnLogin'

    def enter_username(self,username):
        self.dri.find_element_by_id(self.username_textbox_id).clear()
        self.dri.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.dri.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_loginbutton(self):
        self.dri.find_element_by_id(self.submit_button_id).click()