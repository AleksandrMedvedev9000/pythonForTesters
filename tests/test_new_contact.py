# -*- coding: utf-8 -*-
from model.contact import Contact

def test_new_contact(app):
    app.contact.add_new(Contact(first_name="Preved!", middle_name="Bonjour!", last_name="Zdarova!", nickname="Gutentag!", title="Bonapetit",
                                company="Carambol", address="Bodybuild", home_phone="Copperwire", mobile_phone="Budapest",
                                work_phone="Brandenburg", fax="Brontozavr", email="Kremdlyaruk@mail.com", bday="10", bmonth="May",
                                byear="1970", aday="10", amonth="May", ayear="2020", address2="Bodyguard", phone2="Cyberpunk",
                                notes="Hello!"))
