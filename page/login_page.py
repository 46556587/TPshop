from selenium.webdriver.common.by import By

from base import BaseAction

class LoginPage(BaseAction):
    username_button = By.XPATH, "text,请输入手机号码"
    password_button = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_username(self,text):
        self.input(self.username_button,text)

    def input_password(self,text):
        self.input(self.password_button,text)

    def click_login(self):
        self.click(self.login_button)




