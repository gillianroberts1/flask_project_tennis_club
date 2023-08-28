from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
from models.court import Court
import repositories.booking_repository as booking_repository
import repositories.court_repository as court_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)

@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_booking():
    members = member_repository.select_all()
    courts = court_repository.select_all()
    return render_template("bookings/new.html", members=members, courts = courts)

# @bookings_blueprint.route("/bookings", methods=['POST'])
# def create_booking():
#     member_ids = request.form['member_id']
#     court = request.form['court_id']
    # if member_ids length < court capacity
    # loop through each member_id 
    # create booking for each member
    # save each booking
    # redirect to members
    # else redirec to error html page saying court booking is over capacity

@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    member_id = request.form['member_id[]']
    court_id = request.form['court_id']
    member = member_repository.select(member_id)
    court = court_repository.select(court_id)
    booking = Booking(member, court)
    booking_repository.save(booking)
    return redirect('/bookings')

    
    

@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect('/bookings')
