from flask import Flask, render_template, request, redirect
from repositories import member_repository
from repositories import court_repository
from models.court import Court

from flask import Blueprint

courts_blueprint = Blueprint("courts", __name__)
