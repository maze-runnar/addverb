from flask import Flask,render_template,url_for,request,redirect, session
import os
from io import StringIO
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.secret_key = "Remember Red, hope is a good thing maybe the best of the things and no good thing ever dies"
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


from api.api import api_blueprint
import api.routes


app.register_blueprint(api_blueprint)