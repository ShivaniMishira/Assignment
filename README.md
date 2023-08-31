<h3>Description</h3><br>
This project is a simple web application that allows users to create, read, update, and delete (CRUD) data from a database. The database contains information about Id,Name,Email and Role. The web application is built with Django, a Python web framework, and MySql, relational database management system, that connects Python objects to database tables.


<h3>Installation</h3><br>
To install and run this project, you need to have Python 3 and pip installed on your system. You also need to have MySQL,Xammp server, Django installed and running on your system.

<h4>To create the database and tables for this project, you can use the following command:</h4><br>
inside MySQL run the following command:<br>
-- CREATE USER Users@localhost IDENTIFIRD BY 'hello12345';<br>
-- CREATE DATABASE users;<br>
inside terminal run the following command:<br>
-- python manage.py makemigrations<br>
-- python manage.py migrate<br>

This will create a database named 'users' and three tables: Id, Name, Email and Role.

<h3>Worflow</h3><br>
To run the web application, you can use the following command:<br>
python manage.py runserver<br>
This will start a development server on http://127.0.0.1:8000/. You can open this URL in your browser to access the web application.
The web application has five pages :<br>
●   home: this page is front page of webpage.<br>
●   this page returns string "hello world!!".<br>
●	users: This page shows a list of all users in the database. You can click on a "view" to view its details.You can also edit or      delete the book by clicking on the "update" or "Delete " button.<br>
●	Add user: This page allows you to add a new user to the database. You need to enter its Name, Email,  and Role.<br>
●	User Details: This page shows the details of a selected user, such as its Name, Email and Role. <br>
●	update: This page allows you to edit the information of a selected User. You can change its Name, Email, or Role. <br>
●   this web application also has side bar where you can search for user using thair name<br>


<h3>SQL Queries</h3>
This project uses MySQL to interact with the database.<br><br>
to query all books from the database, you can write:<br>
users = Xuser.object.all()<br>
This is equivalent to writing:<br>
SELECT * FROM users;<br><br>
To query users by id, you can write:<br>
user = Xusers.object.filter_by(id=id)<br>
or user = Xusers.object.get(id=id)<br>
This is equivalent to writing:<br>
SELECT * FROM books WHERE id = id;<br><br>
To insert a new user into the database, you can write:<br>
user = Xuser(Name=Name, Email=Email, Role=Role)<>
user.save()<br>
This is equivalent to writing:<br>
INSERT INTO users (Name, Email, Role) VALUES (Name, Email, Role);<br><br>
To update an existing user in the database, you can write:<br>
user = Xusers.objects.get(id=id)<br>
user.Name = Name<br>
user.Email = Email<br>
user.Role = Role<br>
user.save()<br>
This is equivalent to writing:<br><br>
UPDATE users SET Name = Name, Email = Email, Role = Role WHERE id = id;<br>
To delete a user from the database, you can write:<br>
user = Xuser.objects.get(id=id)<br>
user.delete()<br>
This is equivalent to writing:<br>
DELETE FROM users WHERE id = id;<br>

<h3>Contributing to Project Assignment</h3><br>
Thank you for your interest in contributing to Project Assignment! Project X is a web application that allows users to create, read, update, and delete (CRUD) data from a database. We are looking for developers who can help us improve the performance, usability, security and fix bugs of our app.

