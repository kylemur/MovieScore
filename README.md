# Overview

This Movie Score program shows my learning of SQL and relational databases.

There is a menu that allows a user to insert a movie's data into the movies.db database file, update a movie's data, delete a movie, display all movie data, get the average movie score, and see the number of movies in the database.

I have some experience with SQL and databases but I want to learn more and eventually gain experience with noSQL. 


[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

I used SQLite with Python to make a database and then insert, modify, delete, and query data from the database.

Currently there is just one table with columns for title, score, release year, etc.

# Development Environment

Visual Studio Code and SQLite3.

Python and SQL.

# Useful Websites

- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-aggregate-functions/)

# Future Work

- Add more error handling for user input

- Add feature for the user to filter movies by release year, actors, etc.

- Add the following to the database:
### Movies Table
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- title (TEXT, NOT NULL)
- director (TEXT)
- year (INTEGER)
- genre (TEXT)
- rating (REAL)

Reviews Table
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- movie_id (INTEGER, FOREIGN KEY REFERENCES Movies(id))
- review (TEXT)
- score (REAL)

Actors Table
- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- name (TEXT, NOT NULL)
- birthdate (TEXT)

Movie_Actors Table (Many-to-Many relationship between Movies and Actors)
- movie_id (INTEGER, FOREIGN KEY REFERENCES Movies(id))
- actor_id (INTEGER, FOREIGN KEY REFERENCES Actors(id))