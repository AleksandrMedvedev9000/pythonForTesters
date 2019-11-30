# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_name(app):
    app.session.log_in(username="admin", user_password="secret")
    app.group.edit_first(Group(table_name="qqq"))
    app.session.log_out()


def test_edit_first_group_header(app):
    app.session.log_in(username="admin", user_password="secret")
    app.group.edit_first(Group(table_header="222"))
    app.session.log_out()
