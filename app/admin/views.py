# -*- coding: utf-8 -*-

from flask import render_template
from flask_login import login_required, current_user

from . import admin


@admin.route("/", methods=["GET", "POST"])
@login_required
def index():
    print 'c'*100
    print current_user
    return render_template("admin/index.html")
