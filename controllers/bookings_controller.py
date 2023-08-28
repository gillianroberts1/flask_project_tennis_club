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

@bookings_blueprint.route("/bookings/type", methods=['POST'])
def create_booking_type():
    type = request.form['type']
    court = court_repository.select(request.form['court_id'])
    members = member_repository.select_all()
    return render_template("bookings/new-complete.html", type=type, court=court, members=members)


@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    court = request.form['court']
    court = court_repository.select(court)

    print(request.form)
    member_1 = request.form['member-1']
    member_2 = request.form['member-2']
    if 'member-3' in request.form:
        member3 = member_repository.select(request.form['member-3'])
        booking3 = Booking(member3, court)
        booking_repository.save(booking3)
    if 'member-4' in request.form:
        member4 = member_repository.select(request.form['member-4'])
        booking4 = Booking(member4, court)
        booking_repository.save(booking4)

    member1 = member_repository.select(member_1)
    member2 = member_repository.select(member_2)
    booking1 = Booking(member1, court)
    booking2 = Booking(member2, court)
    booking_repository.save(booking1)
    booking_repository.save(booking2)

    return redirect('/bookings')

    
    

@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect('/bookings')
