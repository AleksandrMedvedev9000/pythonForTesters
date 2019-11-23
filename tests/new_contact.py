# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_contact(app):
    app.session.log_in(username="admin", user_password="secret")
    app.add_new_contact(Contact(first_name="Preved!", middle_name="Bonjour!", last_name="Zdarova!", nickname="Gutentag!", title="Bonapetit",
                             company="Carambol", address="Bodybuild", home_phone="Copperwire", mobile_phone="Budapest",
                             work_phone="Brandenburg", fax="Brontozavr", email="Kremdlyaruk@mail.com", bday="10", bmonth="May",
                             byear="1970", aday="10", amonth="May", ayear="2020", address2="Bodyguard", phone2="Cyberpunk",
                             notes="Hello!"))
    app.session.log_out()