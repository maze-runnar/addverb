from api import db
from datetime import datetime, timedelta,date

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), nullable=False)
	content = db.Column(db.String(2000), nullable=False)
	subject = db.Column(db.String(100))
	complete_in = db.Column(db.Integer, default=0)
	date_create = db.Column(db.DateTime, default=datetime.utcnow)
	email = db.Column(db.String(50))
	name = db.Column(db.String(100))
	tags = db.Column(db.String(100))
	points = db.Column(db.Integer(), default=0)

	def __repr__(self):
		return "<task %r> " % self.id

class Answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	answer_id = db.Column(db.Integer, default=1)
	content = db.Column(db.String(2000), nullable=False)
	email = db.Column(db.String(50))
	name = db.Column(db.String(50))

	def __repr__(self):
		return "<task %r> " % self.id

class MySchedule(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	subject = db.Column(db.String(100), default=1)
	topic = db.Column(db.String(2000), nullable=False)
	time = db.Column(db.String(50))
	url = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		return "<task %r> " % self.id


class Student(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, email, password):
        self.email = email
        self.password = password

class Class(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True)
	members = db.Column(db.String(80))

	def __repr__(self):
		return "<task %r> " % self.id

class Attendance(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100))
	subject = db.Column(db.String(100))

	def __repr__(self):
		return "<task %r> " % self.id


db.create_all()