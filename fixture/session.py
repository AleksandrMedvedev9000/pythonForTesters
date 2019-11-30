class SessionHelper:

    def __init__(self, app):
        self.app = app

    def log_out(self):
        wd = self.app.wd
        wd.implicitly_wait(10)
        wd.find_element_by_link_text("Logout").click()
        wd.implicitly_wait(10)

    def log_in(self, username, user_password):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user_password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
