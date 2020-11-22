from flask import Blueprint, jsonify, make_response
from flask_restful import reqparse, request
from api import db
from api.models.models import (
    Student
)

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
            "data": {
                'email': email,
                'password': password
            }
        })
    )