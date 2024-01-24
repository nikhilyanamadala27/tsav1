import os
from flask import Flask,render_template,request
current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(current_dir,"pro.sqlite3")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False