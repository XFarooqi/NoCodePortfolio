from random import random
from flask import Flask, render_template,request,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint, false
app  = Flask(__name__)
# app = Flask(__name__, static_url_path='/assets/Design3')
import uuid
import os , smtplib
app.secret_key = "SecretKey"
from PIL import ImageGrab

# #SQLACHEMY
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/portfolio'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class user(db.Model):
#     sno = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(80),nullable = False)
#     school = db.Column(db.String(80),nullable = False)
#     college = db.Column(db.String(80),nullable = False)
#     phone = db.Column(db.String(80),nullable = False)
#     email = db.Column(db.String(80),nullable = False)
#     about = db.Column(db.String(80),nullable = False)
#     skill1 = db.Column(db.String(80),nullable = False)
#     skill2 = db.Column(db.String(80),nullable = False)
#     skill3 = db.Column(db.String(80),nullable = False)
#     skill4 = db.Column(db.String(80),nullable = False)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/display')
def display():
    return render_template('display.html')

# @app.route('/form')
# def form():
#     return render_template('form.html')

# @app.route('/Design1')
# def Design1():
#     return render_template('Design1.html')

# @app.route('/Design2')
# def Design2():
#     return render_template('Design2.html')
# key = uuid.uuid1()
# img = ImageGrab.grab()
# img_new_name = f"{key}{img.filename}"
# os.rename(f"static/images/{img.filename}", f"static/images/{img_new_name}")
# img.save("random.png")




@app.route("/form/<string:display>", methods = ["GET","POST"])
def form(display):
    session["display_ses"] = display
    return render_template("form.html")

@app.route("/upload", methods = ["GET","POST"])
def upload():
    display_upload = session.get("display_ses")
    if display_upload == "design1":
        display_name = "Design1.html"
    elif display_upload == "design2":
        display_name = "Design2.html"
    elif display_upload == "design3":
        display_name = "Design3.html"
    elif display_upload == "design4":
        display_name = "Design4.html"

    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        name = firstname+lastname
        school = request.form.get("school")
        college = request.form.get("college")
        phone = request.form.get("phone")
        email = request.form.get("email")
        skill1 = request.form.get("skill1")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4 = request.form.get("skill4")
        about = request.form.get("about")
        img = request.form.get("img")

        # entery = user(name = name, school = school, college = college, phone = phone, email = email, about = about, skill1 = skill1, skill2 = skill2, skill3 = skill3)
        # db.session.add(entery)
        # db.session.commit()

# Email 
        subject = "Congratulations!" + " " + firstname +""+ lastname
        body = "You will get the Working Link of You Website Shortly!"
        msg = f'Subject: {subject}\n\n{body}'
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("arfarooqix@gmail.com","qjxlzmkgjgglqkgp")
        server.sendmail("arfarooqix@gmail.com",email,msg)

        

#Assigning Ids to Images
        key = uuid.uuid1()
        img = request.files["dp"]
        img.save(f"static/images/{img.filename}")
        img_new_name = f"{key}{img.filename}"
        os.rename(f"static/images/{img.filename}", f"static/images/{img_new_name}")
    return render_template(display_name,t_fname = firstname,t_lname=lastname,school = school,college = college, phone = phone, email = email, skill1 = skill1, skill2 = skill2, skill3 = skill3, skill4 = skill4, about = about, img = img_new_name)

    


if __name__ == '__main__':
    app.run(debug = True)




