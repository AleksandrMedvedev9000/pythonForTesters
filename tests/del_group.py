# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create_new(Group(table_name="", table_header="", table_footer=""))
    app.group.delete_first()
