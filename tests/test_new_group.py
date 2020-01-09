# -*- coding: utf-8 -*-
from model.group import Group


def test_new_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new(Group(table_name="Preved!", table_header="Bonjour!", table_footer="Zdarova!"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_new_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new(Group(table_name="", table_header="", table_footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
