# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == "0":
        app.contact.add_new(Contact())
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == int(app.contact.count())
    del old_contacts[0]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
