from flask import Blueprint, jsonify, make_response, session
from flask_restful import reqparse, request
from api import db
from api.models.models import (
    Student,
    MySchedule,
    Attendance,
    Todo
)

from datetime import datetime, timedelta

api_blueprint = Blueprint('api','api', url_prefix='/api')

# @route = '/api/
# index page
def index():
    return "Hello World!"

# @route: '/api/register-student/
# regsiter student
def RegisterStudent():
    # adding parsing rules
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('email', help='This field cannot be blank', required=True,)
    parser.add_argument('password', help="This field cannot be blank", required=True)

    # parsing incoming rquest data
    args = parser.parse_args()
    email = args['email']
    password = args['password']

    new_user = Student(email=email,password=password)
    print(new_user)
    db.session.add(new_user)
    db.session.commit()

    return make_response(
        jsonify({
            "status": 'success',
            "logged_in": True,
            "data": {
                'email': email,
                'password': password
            }
        })
    )

def AllStudents():
	allstudents = db.session.query(Student).all()
	db.session.commit()
	return make_response(
        jsonify({
            "allstudents": allstudents
        })
    )

def Logout():
	session['logged_in'] = False
	session["teacher_logged_in"] = False
	return make_response(
        jsonify({
            "logged_in": False
        })
    )


def CurrentClass():
    allclasses = db.session.query(MySchedule).all()
    upcoming_classes = []
    previous_classes = []
    for i in allclasses:
        t = i.time.split("T")
        x = str(datetime.utcnow()).split(" ")
        current_time_hour = x[1][0:2]
        current_time_min = x[1][3:5]
        current_time_date = x[0]
        class_time_hour = t[1][0:2]
        class_time_min = t[1][3:5]
        class_time_date = t[0]
        if(current_time_hour > class_time_hour or class_time_date < current_time_date):
            previous_classes.append(i)
        else:
            upcoming_classes.append(i)

    return make_response(
        jsonify({
        "previous_classes": previous_classes,
        "upcoming_classes": upcoming_classes
        })
        )


def attendance(id):
	if request.method == "POST":
		my_subject = db.session.query(MySchedule).filter_by(id = id).first()
		my_subject_name = my_subject.subject
		url = my_subject.url
		std_email = session["student_email"]
		new_attendee = Attendance(email=std_email, subject=my_subject_name)
		try:
			db.session.add(new_attendee)
			db.session.commit()
			return make_response(
                jsonify({
                    "status": "success",
                    data:{
                        "meeting-url": url
                    }
                })
            )
		except:
			return "error is here"
	else:
		return make_response(
            jsonify({
                "get_current_class": "/current-class"
            })
        )
	

def AddQuestion():
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('title', help='This field cannot be blank', required=True,)
    parser.add_argument('task_content', help="This field cannot be blank", required=True)

    # parsing incoming rquest data
    args = parser.parse_args()
    # email = args['email']
    # password = args['password']
    title = args["title"]
    task_content = args['content']
    complete_in = args["completetime"]
    subject = args["subject"]
    email= args["email"]
    name = args["std_name"]
    tags = args["tags"]
    new_task = Todo(title=title,content=task_content,subject=subject,complete_in=complete_in,email=email, name=name, tags=tags)
    try:
        db.session.add(new_task)
        db.session.commit()
        return make_response(
            jsonify({
                "status": "success",
                "data" : {
                    "title": title,
                    "content": task_content,
                    "complete_in": complete_in,
                    "subject": subject,
                    "email": email,
                    "name":name,
                    "tags": tags
                }
            })
        )
    except:
        return "there was an error in adding your task"

def AllQuestions():
    tasks = Todo.query.order_by(Todo.date_create).all()
    new_tasks = []
    previous_tasks = []
    for i in tasks:
        if i.date_create + timedelta(days=i.complete_in) >  datetime.utcnow():
            new_tasks.append(i)
        else:
            previous_tasks.append(i)

    return make_response(
        jsonify({
            "new_task": new_tasks,
            "previous_tasks": previous_tasks
        })
    )