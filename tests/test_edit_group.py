# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create_new(Group(table_name="", table_header="", table_footer=""))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(table_name="qqq"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create_new(Group(table_name="", table_header="", table_footer=""))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(table_header="222"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
