import os

import pytest
import sys
sys.path.append(os.getcwd())

from page.login_page import LoginPage


class TestLogin:
    def setup(self):
        self.login_page = LoginPage()

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @pytest.mark.parametrize("username, password", [("zhangsan", "123456"),("lisi", "123"),("wangwu", "654321")])
    def test_login(self, username, password):
        self.login_page.input_name(username)
        self.login_page.input_password(password)
        self.login_page.click_input()
        assert 1
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username, password", [("zhangsan", "123456"), ("lisi", "123"), ("wangwu", "654321")])
    def test_login2(self,username, password):
        self.login_page.input_password(password)
        self.login_page.input_name(username)
        self.login_page.click_input()
        assert 1