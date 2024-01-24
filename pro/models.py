from flask_sqlalchemy import SQLAlchemy
from other import app


dbs= SQLAlchemy(app)
class Userlogin(dbs.Model):
    __tablename__ = "userlogin"
   
    usname1=dbs.Column(dbs.String)
 
    pass1=dbs.Column(dbs.String)
    uid=dbs.Column(dbs.Integer,autoincrement=True,primary_key=True)
class Adminlogin(dbs.Model):
    __tablename__ = "adminlogin"
    usname=dbs.Column(dbs.String)
    aid=dbs.Column(dbs.Integer,autoincrement=True,primary_key=True)
    pass0=dbs.Column(dbs.String)
    
class Venue(dbs.Model):
    __tablename__ = "venuet"
    venue=dbs.Column(dbs.String)
    vid=dbs.Column(dbs.Integer,autoincrement=True,primary_key=True)
    loc=dbs.Column(dbs.String)
    cap=dbs.Column(dbs.Integer)
    showz= dbs.relationship('Show', backref='showt')
class Show(dbs.Model):
    __tablename__ = "showt"
    showname=dbs.Column(dbs.String)
    sid=dbs.Column(dbs.Integer,autoincrement=True,primary_key=True)
    rating=dbs.Column(dbs.Integer)
    genre=dbs.Column(dbs.String)
    runtime=dbs.Column(dbs.Integer)
    uu = dbs.Column(dbs.Integer, dbs.ForeignKey("venuet.vid"))
    bookings=dbs.Column(dbs.Integer)
class Feedback(dbs.Model):
    __tablename__ = "feedbackt"
    
    feedid=dbs.Column(dbs.Integer,autoincrement=True,primary_key=True)
    
    feedback=dbs.Column(dbs.String)
   