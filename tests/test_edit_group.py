# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_name(app):
    pre_groups = app.group.get_group_list()
    if len(pre_groups) == 0:
        app.group.create_new(Group(table_name="", table_header="", table_footer=""))
    old_groups = app.group.get_group_list()
    group = Group(table_name="qqq")
    group.table_id = old_groups[0].table_id
    app.group.edit_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_header(app):
#    pre_groups = app.group.get_group_list()
#    if len(pre_groups) == 0:
#        app.group.create_new(Group(table_name="", table_header="", table_footer=""))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first(Group(table_header="222"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
