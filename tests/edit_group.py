# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    app.session.log_in(username="admin", user_password="secret")
    app.group.edit_first(Group(table_name="111", table_header="222", table_footer="333"))
    app.session.log_out()