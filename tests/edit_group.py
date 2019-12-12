# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create_new(Group(table_name="", table_header="", table_footer=""))
    app.group.edit_first(Group(table_name="qqq"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create_new(Group(table_name="", table_header="", table_footer=""))
    app.group.edit_first(Group(table_header="222"))
