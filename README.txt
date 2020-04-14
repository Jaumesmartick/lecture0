###########################################################################################
                            HTML LINKS
###########################################################################################

aboutus.html => Description of the project, company and some link information to contact us
bootstrap.html => Link to try new bootstrap features 
courses.html => Link to show the courses available in the webpage (description and offers)
home.html => HomePage when looking for Aula, short introduction and description
layout.html => Main structure of the website to be imported in most of the links
login.html => Link for login after create an user
name.html => Link of trial to show how to change the URL with some condition and say hello to a specific user
pruebas.html => Link to try new features and structures of HTML and courses
register.html => Link to register a new user within the website

###########################################################################################
                            CSS LINKS
###########################################################################################

courses.css =>
homepage.css =>
pruebas.css =>
register.css =>

###########################################################################################
                            PYTHON LINKS
###########################################################################################

hello.py => Structure created with FLASK to manage the links between the different pages and
            the information received/sent for the input/output shown in the html.
list.py => Trial of the connection between the python code and the database

###########################################################################################
                            FUTURE WORK
###########################################################################################

1. Register the users in the database (DONE)
2. Confirm the password when registering (DONE)
3. Confirm the username is not used when registering (DONE)
4. Confirm the email is not used when registering (DONE)
5. Introduce the courses in database
6. Link the courses database with the students
7. Change the classes to be unique and change the css to show the required output for every div,h1,etc.
8. Use the Javascript tools to pop-up a message when : 
    e.g. the registration fails 
9. Connect the database to VisualStudio


###########################################################################################
                            ERRORS
###########################################################################################

1. When importing the html layout in every html:
    " RecursionError: maximum recursion depth exceeded in comparison" ERRROR APPEARS 
    SOLUTION: I introduced the html link into the own html template, what created a unnecesary loop that made the system breaks.
2. Problem wiht the create_engine function 
    SOLUTION: Install psycopg2 and introduce the url where the database is held.
3. Cannot use bootstrap when importing the html layout 
    SOLUTION: Don't use the same names for classes as bootstrap does
4. Cannot conect the postgresql to VisualStudio

###########################################################################################
                            DATABASES
###########################################################################################

1. alumnos
    a.username
    b.first_name
    c.last_name
    d.email
    e.password
    f.edad

2.courses   
    a. name
    b. price
    c. edad
    d. description
    e. categoria
    f. spec_offer
