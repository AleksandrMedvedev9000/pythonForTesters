# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_contact(app):
    app.session.log_in(username="admin", user_password="secret")
    app.contact.edit_first(Contact(first_name="111", middle_name="222", last_name="333", nickname="444", title="555",
                                company="666", address="777", home_phone="888", mobile_phone="999",
                                work_phone="000", fax="", email="", bday="10", bmonth="May",
                                byear="1970", aday="10", amonth="May", ayear="2020", address2="", phone2="",
                                notes=""))
    app.session.log_out()