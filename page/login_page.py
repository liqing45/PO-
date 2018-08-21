import allure



class LoginPage:
    @allure.step(title="输入姓名")
    def input_name(self, username):
        allure.attach("输入姓名：", username)
        print(username)

    @allure.step(title="输入密码")
    def input_password(self, password):
        allure.attach("输入密码：", password)
        print(password)

    @allure.step(title="点击登陆")
    def click_input(self):
        print("click")