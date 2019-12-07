# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_name(app):
    app.group.edit_first(Group(table_name="qqq"))


def test_edit_first_group_header(app):
    app.group.edit_first(Group(table_header="222"))
