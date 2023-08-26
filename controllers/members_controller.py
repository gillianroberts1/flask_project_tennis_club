from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.member import Member

import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)



@members_blueprint.route("/members")
def members_list():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)


# route show single member GET members/<id>

@members_blueprint.route("/members/<id>")
def show_member(id):
    member = member_repository.select(id)
    return render_template("members/show.html", member=member)


# route to add new member GET




#route to edit exiting member GET members/<id>/edit


# update PUT /memebrs/<id>




# route to mark member as acive/deactive

