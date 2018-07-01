from base.base_driver import init_driver
from page.page import Page

class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page=Page(self.driver)

    def test_login1(self):
        # 首页点击我的
        self.page.home.click_mine()
        # 我的页面点击登录/注册
        self.page.mine.click_login_signup()
        # 登录页面输入用户名
        self.page.login.input_username("18883879403")
        # 登录页面输入密码
        self.page.login.input_password("123456")
        # 登录点击登录
        self.page.login.click_login()

        