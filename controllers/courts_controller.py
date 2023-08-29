from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.court import Court

import repositories.court_repository as court_repository
import repositories.member_repository as member_repository

courts_blueprint = Blueprint("courts", __name__)

@courts_blueprint.route("/courts")
def courts_list():
    booked_courts = court_repository.courts_with_bookings()
    unbooked_courts = court_repository.courts_with_no_bookings()
    return render_template("courts/index.html", booked_courts=booked_courts, unbooked_courts=unbooked_courts)

@courts_blueprint.route("/courts/<id>")
def show_court(id):
    court = court_repository.select(id)
    members = member_repository.members_for_court(court)
    return render_template("courts/show.html", court=court, members=members)

@courts_blueprint.route("/courts/new")
def new_court():
    return render_template('courts/new.html')

@courts_blueprint.route("/courts", methods=['POST'])
def create_court():
    court_no = request.form['court_no']
    surface = request.form['surface']
    court = Court(court_no, surface)
    court_repository.save(court)
    return redirect('/courts')

@courts_blueprint.route("/courts/<id>/edit")
def edit_court(id):
    court = court_repository.select(id)
    return render_template("courts/edit.html", court=court)

@courts_blueprint.route("/courts/<id>", methods=['POST'])
def update_court(id):
    court_no = request.form['court_no']
    surface = request.form['surface']
    court = Court(court_no, surface, id)
    court_repository.update(court)
    return redirect('/courts')

