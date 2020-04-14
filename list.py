import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:16aroa01.@localhost/postgres", pool_pre_ping=True) #DATABASE_URL
db = scoped_session(sessionmaker(bind=engine))

def main(): #Function to show the users in the db
        users = db.execute("SELECT username FROM alumnos").fetchall()
        for user in users:
            print(f"Username: {user.username}")
def importar(): #Function to introduce some new users from csv file
        f = open("alumnos.csv")
        reader = csv.reader(f)
        for user, first, last, email, passw in reader:
            db.execute("INSERT INTO alumnos(username, first_name, last_name, email, password) VALUES (:username,:first_name,:last_name,:email,:password)",
            {"username": user, "first_name":first, "last_name":last, "email":email,"password":passw})
            print(f"Nuevo alumno añadido: {user}")  
        db.commit()
if __name__=="__main__":
    importar()