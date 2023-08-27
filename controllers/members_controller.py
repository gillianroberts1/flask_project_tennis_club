from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.member import Member

import repositories.member_repository as member_repository
import repositories.court_repository as court_repository

members_blueprint = Blueprint("members", __name__)



@members_blueprint.route("/members")
def members_list():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)


# route show single member GET members/<id>

@members_blueprint.route("/members/<id>")
def show_member(id):
    member = member_repository.select(id)
    courts = court_repository.court_for_member(member)
    return render_template("members/show.html", member=member, courts=courts)


# route to add new member GET
@members_blueprint.route("/members/new")
def new_user():
    return render_template('members/new.html')


# create POST'/members'
@members_blueprint.route("/members", methods=['POST'])
def create_member():
    name = request.form['name']
    address = request.form['address']
    postcode = request.form['postcode']
    tel_no = request.form['tel_no']
    email = request.form['email']
    dob = request.form['dob']
    premium = request.form['premium']
    member = Member(name, address, postcode, tel_no, email, dob, premium)
    member_repository.save(member)
    return redirect('/members')


#route to edit exiting member GET members/<id>/edit
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member=member)

# update PUT /members/<id>
@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    name = request.form['name']
    address = request.form['address']
    postcode = request.form['postcode']
    tel_no = request.form['tel_no']
    email = request.form['email']
    dob = request.form['dob']
    premium = request.form['premium']
    member = Member(name, address, postcode, tel_no, email, dob, premium, None, None, id)
    member_repository.update(member)
    return redirect('/members')






# route to mark member as acive/deactive

