from flask import Flask
from flask_restful import Resource, fields, marshal_with, reqparse

from models import dbs
from models import Venue,Show
from validation import NotFoundError, BusinessValidationError

venue_fields = {
    'venue': fields.String,
    'vid': fields.Integer,
    'loc': fields.String,
    'cap': fields.Integer,
    'showz' : fields.String
}

v_parser = reqparse.RequestParser()
v_parser.add_argument('venue')
v_parser.add_argument('loc')
v_parser.add_argument('cap')


vu_parser = reqparse.RequestParser()
vu_parser.add_argument('venue')
vu_parser.add_argument('cap')
vu_parser.add_argument('loc')
class VAPI(Resource):
    @marshal_with(venue_fields)
    def get(self, venuein):
       # venueget = dbs.session.query(Venue).filter(Venue.venue==venuein).first()
        
        venueget = Venue.query.get(venuein)
        if venueget:
           return venueget
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(venue_fields)
    def post(self):
        args = v_parser.parse_args()
        venue = args.get('venue', None)
        loc = args.get('loc', None)
        cap = args.get('cap', None)
   
        

        if venue is None:
            raise BusinessValidationError(status_code=400, error_code='001', error_message=' Name is required')
        if loc is None:
            raise BusinessValidationError(status_code=400, error_code='001', error_message=' loc is required')
        if cap is None:
            raise BusinessValidationError(status_code=400, error_code='001', error_message=' cap is required')
       
        venuepost = dbs.session.query(Venue).filter(Venue.venue==venue).first()
        if venuepost:
            raise BusinessValidationError(status_code=400, error_code='002', error_message=' Name already exists')
        
        l = Venue(venue=venue, loc=loc,cap=cap)
        dbs.session.add(l)
        dbs.session.commit()
        return l, 201

    def delete(self, venuein):
        l = Venue.query.get(venuein)
        if l is None:
            raise NotFoundError(status_code=404)
        else:
            dbs.session.delete(l)
            dbs.session.commit()
            return "Successfully Deleted"

    @marshal_with(venue_fields)
    def put(self, venuein):
        l = Venue.query.get(venuein)
        if l is None:
            raise NotFoundError(status_code=404)

        args = vu_parser.parse_args()
         
        l.venue = args.get('venue')
        l.cap = args.get('cap')
        
        l.loc = args.get('loc')
        dbs.session.commit()
        return l,200
       



show_fields = {
    'sid': fields.Integer,
    'genre': fields.String,
    'showname': fields.String,
    'booking': fields.Integer,
    
}

s_parser = reqparse.RequestParser()
s_parser.add_argument('rating')
s_parser.add_argument('showname')
s_parser.add_argument('runtime')
s_parser.add_argument('genre')
s_parser.add_argument('sid')
s_parser.add_argument('booking')


su_parser = reqparse.RequestParser()
su_parser.add_argument('rating')
su_parser.add_argument('genre')
su_parser.add_argument('bookings')
class SAPI(Resource):
    @marshal_with(show_fields)
    def get(self, showin):
        showget = Show.query.get(showin)
         
        

        
        
        if showget:
           return showget
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(show_fields)
    def post(self):
        args = s_parser.parse_args()
        showname = args.get('showname', None)
        
        genre = args.get('genre', None)
        
        if showname is None:
            raise BusinessValidationError(status_code=400, error_code='001', error_message=' Name is required')
        
        if genre is None:
            raise BusinessValidationError(status_code=400, error_code='001', error_message=' genre is required')
       
        showpost = dbs.session.query(Show).filter(Show.showname==showname).first()
        if showpost:
            raise BusinessValidationError(status_code=400, error_code='002', error_message=' Name already exists')
        
        l = Show(showname=showname, genre=genre)
        dbs.session.add(l)
        dbs.session.commit()
        return "", 201

    def delete(self, showin):
        l = Show.query.get(showin)
        if l is None:
            raise NotFoundError(status_code=404)
        else:
            dbs.session.delete(l)
            dbs.session.commit()
            return "Successfully Deleted"

    @marshal_with(show_fields)
    def put(self, showin):
        l = Show.query.get(showin)
        
        if l is None:
            raise NotFoundError(status_code=404)

        args = su_parser.parse_args()
         
        l.showname = args.get('rating')
        l.genre = args.get('genre')
        
        l.bookings = args.get('bookings')
        dbs.session.commit()
        return l,200

       
