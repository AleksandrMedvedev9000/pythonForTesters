# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_some_group_name(app):
    pre_groups = app.group.get_group_list()
    if len(pre_groups) == 0:
        app.group.create_new(Group(table_name="", table_header="", table_footer=""))
    old_groups = app.group.get_group_list()
    group = Group(table_name="qqq")
    index = randrange(len(old_groups))
    group.table_id = old_groups[index].table_id
    app.group.edit_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_header(app):
#    pre_groups = app.group.get_group_list()
#    if len(pre_groups) == 0:
#        app.group.create_new(Group(table_name="", table_header="", table_footer=""))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first(Group(table_header="222"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
