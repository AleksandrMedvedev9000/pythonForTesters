# -*- coding: utf-8 -*-
from model.group import Group

def test_new_group(app):
    app.session.log_in(username="admin", user_password="secret")
    app.group.create_new(Group(table_name="Preved!", table_header="Bonjour!", table_footer="Zdarova!"))
    app.session.log_out()

def test_new_empty_group(app):
    app.session.log_in(username="admin", user_password="secret")
    app.group.create_new(Group(table_name="", table_header="", table_footer=""))
    app.session.log_out()
