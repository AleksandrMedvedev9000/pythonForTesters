# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_group(app):
    app.session.log_in(username="admin", user_password="secret")
    app.create_new_group(Group(table_name="Preved!", table_header="Bonjour!", table_footer="Zdarova!"))
    app.session.log_out()


def test_new_empty_group(app):
    app.session.log_in(username="admin", user_password="secret")
    app.create_new_group(Group(table_name="", table_header="", table_footer=""))
    app.session.log_out()
