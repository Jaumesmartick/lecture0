import datetime
from flask import Flask, render_template, request,session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:16aroa01.@localhost/postgres", pool_pre_ping=True) #DATABASE_URL
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"] = "fylesystem" # It save the information stored in the session
Session(app) #With session you have specific information for your profile

@app.route("/")
def home():
    now = datetime.datetime.now()
    return render_template("home.html",date=now)

#REGISTER USERS IN THE DATABASE
@app.route("/register",methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        #course = request.form.get("courses")# FUTURE WORK: Introduce the course as a new table
        email = request.form.get("email")
        #Check the password
        if password1 != password2 : 
            return render_template("register.html", message="ERROR: The password introduced in both boxes is not the same")
        elif db.execute("SELECT * FROM alumnos WHERE email= :email",{"email": email}).rowcount>0:
            return render_template("register.html", message="ERROR: The email introduced is already registered")
        elif db.execute("SELECT * FROM alumnos WHERE username= :username",{"username": username}).rowcount>0:
            return render_template("register.html", message="ERROR: The username is already taken, please choose a different one")
        else:
            db.execute("INSERT INTO alumnos(username, first_name, last_name, email, password) VALUES (:username,:first_name,:last_name,:email,:password)",
            {"username": username, "first_name":first_name, "last_name":last_name, "email":email,"password":password1})
            print(f"Nuevo alumno añadido: {username}")
        db.commit()
        User = {"username":username,"first_name":first_name,"last_name":last_name,"password":password1,"email":email}
        return render_template("regcompleted.html",user=User)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/registercourses")
def reg_courses():
    return render_template("regcourses.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/pruebas")
def pruebas():
    return render_template("pruebas.html")

@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")

@app.route("/<string:name>")
def personal(name):
    name=name.capitalize() #The first letter in capital 
    #return f"<h1> Hello {name}<h1>"
    return render_template("name.html",name=name)
