# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group

class NewGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_new_group(self):
        wd = self.wd
        self.open_main_page(wd)
        self.log_in(wd, username="admin", user_password="secret")
        self.open_group_page(wd)
        self.create_new_group(wd, Group(table_name="Preved!", table_header="Bonjour!", table_footer="Zdarova!"))
        self.open_group_page(wd)
        self.log_out(wd)

    def test_new_empty_group(self):
        wd = self.wd
        self.open_main_page(wd)
        self.log_in(wd, username="admin", user_password="secret")
        self.open_group_page(wd)
        self.create_new_group(wd, Group(table_name="", table_header="", table_footer=""))
        self.open_group_page(wd)
        self.log_out(wd)

    def log_out(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_new_group(self, wd, group):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.table_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.table_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.table_footer)
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def log_in(self, wd, username, user_password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user_password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_main_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
