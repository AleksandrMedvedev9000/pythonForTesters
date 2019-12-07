# -*- coding: utf-8 -*-
from model.group import Group


def test_new_group(app):
    app.group.create_new(Group(table_name="Preved!", table_header="Bonjour!", table_footer="Zdarova!"))


def test_new_empty_group(app):
    app.group.create_new(Group(table_name="", table_header="", table_footer=""))
