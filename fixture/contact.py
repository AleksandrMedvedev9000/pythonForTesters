from selenium.webdriver.support.select import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        self.open_create_contact_page()
        self.fill_contact_fields(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_home_page()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        self.check_and_type("firstname", contact.first_name)
        self.check_and_type("middlename", contact.middle_name)
        self.check_and_type("lastname", contact.last_name)
        self.check_and_type("nickname", contact.nickname)
        self.check_and_type("title", contact.title)
        self.check_and_type("company", contact.company)
        self.check_and_type("address", contact.address)
        self.check_and_type("home", contact.home_phone)
        self.check_and_type("mobile", contact.mobile_phone)
        self.check_and_type("work", contact.work_phone)
        self.check_and_type("fax", contact.fax)
        self.check_and_type("email", contact.email)
        self.check_and_type_dropdowns("bday", contact.bday)
        self.check_and_type_dropdowns("bmonth", contact.bmonth)
        self.check_and_type("byear", contact.byear)
        self.check_and_type_dropdowns("aday", contact.aday)
        self.check_and_type_dropdowns("amonth", contact.amonth)
        self.check_and_type("ayear", contact.ayear)
        self.check_and_type("address2", contact.address2)
        self.check_and_type("phone2", contact.phone2)
        self.check_and_type("notes", contact.notes)

    def check_and_type_dropdowns(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def check_and_type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def edit_first(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//tbody/tr[2]/td[8]/a").click()
        self.fill_contact_fields(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()

    def count(self):
        wd = self.app.wd
        return wd.find_element_by_id("search_count").text
