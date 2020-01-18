# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    if app.contact.count() == "0":
        app.contact.add_new(Contact())
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == int(app.contact.count())
    del old_contacts[index]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
