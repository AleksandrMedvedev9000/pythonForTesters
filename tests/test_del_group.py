# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_first_group(app):
    pre_groups = app.group.get_group_list()
    if len(pre_groups) == 0:
        app.group.create_new(Group(table_name="", table_header="", table_footer=""))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
