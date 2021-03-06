# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == "0":
        app.contact.add_new(Contact())
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="111", middle_name="222", last_name="333", nickname="444", title="555",
                                company="666", address="777", home_phone="888", mobile_phone="999", work_phone="000",
                                fax="", email="", bday="10", bmonth="May", byear="1970", aday="10", amonth="May",
                                ayear="2020", address2="", phone2="", notes="")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_by_index(contact, index)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == int(app.contact.count())
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_edit_middle_name_contact(app):
#    if app.contact.count() == "0":
#        app.contact.add_new(Contact())
#    old_contacts = app.contact.get_contacts_list()
#    app.contact.edit_first(Contact(middle_name="qqq"))
#    new_contacts = app.contact.get_contacts_list()
#    assert len(old_contacts) == len(new_contacts)
