from flask import Flask,render_template,request
from other import app
from flask_restful import Resource, Api
from api import VAPI,SAPI
from models import Userlogin,Adminlogin,Show,Venue,dbs,Feedback
import json
api=None





api=Api(app)

api.add_resource(VAPI,"/api/venueget/<int:venuein>","/api/venuepost","/api/venuedelete/<int:venuein>","/api/venueput/<int:venuein>")
api.add_resource(SAPI,"/api/showget/<int:showin>","/api/showpost","/api/showdelete/<int:showin>","/api/showput/<int:showin>")



@app.route('/')
def home():
    return render_template('home.html')
# Define routes
          
        
        

@app.route('/admin',methods=['GET','POST'])
def admin():
   if request.method == 'GET':
        
       return render_template('admin.html')
   elif request.method == 'POST':
        admin_name = request.form['NAME']
        admin_pass =request.form['PASSWORD']
       

        if  admin_name=='NIKHIL' and admin_pass=='hii':
            
          
          
            y=Adminlogin(usname = request.form['NAME'], pass0 = request.form['PASSWORD'])
            dbs.session.add(y)
            dbs.session.commit()
         
        
            venues=Venue.query.all()
            return render_template('venuedisp.html',venues=venues)
        else:
            return render_template('admin.html')




@app.route('/find',methods=['POST'])
def find():
    
    if request.method == 'POST':

          loc=request.form['FIND']

          

          venues = Venue.query.filter_by(loc=loc).all()
          

    return render_template('venuedisp.html', venues=venues)
@app.route('/findu',methods=['POST'])
def findu():
    
    if request.method == 'POST':

          showna=request.form['FIND']

          

          shows = Show.query.filter_by(showname=showna).all()
          

    return render_template('showdispu.html', shows=shows)

@app.route('/reg')
def reg():
    return render_template('reg.html')

@app.route('/venue' , methods = ['GET','POST'])
def venue():
     if request.method == 'GET':
        
       return render_template('venue.html')
     elif request.method == 'POST':
          
          
          s=Venue(venue = request.form['NAME'], loc = request.form['LOCATION'],cap =request.form['CAPACITY'])
          dbs.session.add(s)
          dbs.session.commit()
          
          venues=Venue.query.all()
          return render_template('venuedisp.html',venues=venues)
@app.route('/venuedelete/<int:vid>', methods=['GET','POST'])
def venuedelete(vid):
         venued=Venue.query.filter_by(vid = vid).first()
         dbs.session.delete(venued)
         dbs.session.commit()
         venues=Venue.query.all()
         return render_template('venuedisp.html',venues=venues)
     
@app.route('/venueedit/<int:vid>', methods=['GET','POST'])
def venueedit(vid):
         venuet=Venue.query.filter_by(vid = vid).first()
         if request.method == 'GET':
             return render_template("venuedup.html",venuet=venuet)
         elif request.method == 'POST':
             e=venuet.vid
         
             dbs.session.delete(venuet)
             s=Venue(vid = e, venue = request.form["NAME"],loc = request.form['LOCATION'],cap =request.form['CAPACITY'])
             dbs.session.add(s)
             dbs.session.commit()
             venues=Venue.query.all()
             return render_template('venuedisp.html',venues=venues)

@app.route('/s/<int:vid>',methods = ['GET','POST'])
def show(vid):
     tt=vid
     venuet=Venue.query.filter_by(vid=vid).first()
     
     if request.method == 'GET':
       
       return render_template('show.html', venuet=venuet)
     elif request.method == 'POST':
          
          
          st=Show(uu=tt ,bookings=request.form['B'],showname = request.form['NAME'], rating = request.form['RATING'],genre =request.form['TYPE'],runtime=request.form['RT'])
          dbs.session.add(st)
          dbs.session.commit()
          
          shows=venuet.showz
          print (shows,venuet)
          return render_template('showdisp.html', venuet=venuet, shows=shows)


@app.route('/show/<int:vid>',methods = ['GET','POST'])
def show4(vid):
     tt=vid
     venuet=Venue.query.filter_by(vid=vid).first()
     
     if request.method == 'GET':
       shows=venuet.showz
       return render_template('showdisp.html', venuet=venuet, shows=shows)
     
@app.route('/showdelete/<int:sid>/<int:vid>', methods=['GET','POST'])
def showdelete(sid,vid):
            
            showt=Show.query.filter_by(sid=sid).first()
        
            venuet=Venue.query.filter_by(vid=vid).first()
            dbs.session.delete(showt)
            
            
            dbs.session.commit()
            shows=venuet.showz
            
            return render_template('showdisp.html',showt=showt,venuet=venuet,shows=shows)
     
     
@app.route('/showedit/<int:sid>/<int:vid>', methods=['GET','POST'])
def showedit(sid,vid):
         
         venuet=Venue.query.filter_by(vid=vid).first()
         showt=Show.query.filter_by(sid = sid).first()
         if request.method == 'GET':
             return render_template("showdup.html",venuet=venuet,showt=showt)
         elif request.method == 'POST':
             e=showt.sid
             b=showt.bookings
             #showt.rating=request.form['RATING']
            #  showt.genre=request.form['TYPE']
            #  showt.showname=request.form['NAME']
            #  showt.
             dbs.session.delete(showt)
             sc=Show(sid = e,bookings=b,showname=request.form['NAME'] ,rating = request.form['RATING'],genre =request.form['TYPE'],runtime =request.form['RT'])
             dbs.session.add(sc)
             dbs.session.commit()
             shows=venuet.showz
            
             return render_template('showdisp.html',showt=showt,venuet=venuet,shows=shows)

@app.route('/user',methods=['GET','POST'])
def user():
    if request.method == 'GET':
        
       return render_template('user.html')
    elif request.method == 'POST':
        user_name = request.form['NAME']

        user = Userlogin.query.filter_by(usname1=user_name).first()

        if user==None:
            
          
          
            x=Userlogin(usname1 = request.form['NAME'], pass1 = request.form['PASSWORD'])
            dbs.session.add(x)
            dbs.session.commit()
         
          
          
          
            venues=Venue.query.all()
            return render_template('userdisp.html',venues=venues)
        else:
            venues=Venue.query.all()
            return render_template('userdisp.html',venues=venues)

@app.route('/user/<int:vid>',methods=['GET','POST'])
def user1(vid):
    venue=Venue.query.filter_by(vid=vid).first()
    shows=venue.showz
    if request.method == 'GET':
        
       return render_template('showdispu.html',shows=shows)   

    

@app.route('/booking/<int:sid>',methods=['GET','POST'])
def book(sid):
    show=Show.query.filter_by(sid=sid).first()
   
    if request.method == 'GET':
       print(show.bookings)  
       return render_template('booking.html',show=show)
    
    else:
        available=show.bookings
        
        
        if available < int(request.form['TICKETS']):
            return render_template('booking.html',show=show,message="enter valid number")
           
        else:
            show.bookings-=int(request.form['TICKETS'])
            dbs.session.commit()
            return render_template('booking.html',show=show,message="booking sucessful")
@app.route('/feed',methods=['GET','POST'])
def feed():
    if request.method == 'GET':
       return render_template('feed.html')
    elif request.method == 'POST':
          
          
          f=Feedback(feedback = request.form['F'])
          dbs.session.add(f)
          dbs.session.commit()
          venues=Venue.query.all()
          
          
          return render_template('userdisp.html',venues=venues)


@app.route('/sum')
def sum():
       
        sh = Show.query.all()
        (labels, bookings) = ([], [])
        for l in sh:
            labels.append(l.showname)
            bookings.append(l.bookings)
            
            
       
       
        return render_template('sum.html',labels = json.dumps(labels), bookings= json.dumps(bookings)   )
   
     
      
if __name__=='__main__':
   app.run(debug=True)
