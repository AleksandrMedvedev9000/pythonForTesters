# -*- coding: utf-8 -*-
from model.contact import Contact

def test_new_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="Preved!", middle_name="Bonjour!", last_name="Zdarova!", nickname="Gutentag!", title="Bonapetit",
                                company="Carambol", address="Bodybuild", home_phone="Copperwire", mobile_phone="Budapest",
                                work_phone="Brandenburg", fax="Brontozavr", email="Kremdlyaruk@mail.com", bday="10", bmonth="May",
                                byear="1970", aday="10", amonth="May", ayear="2020", address2="Bodyguard", phone2="Cyberpunk",
                                notes="Hello!")
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
