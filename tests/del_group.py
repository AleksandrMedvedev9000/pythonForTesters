# -*- coding: utf-8 -*-
def test_delete_first_group(app):
    app.session.log_in(username="admin", user_password="secret")
    app.group.delete_first()
    app.session.log_out()