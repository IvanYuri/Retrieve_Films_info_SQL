As part of studies inside Data Science this is a SQL exercise conducted by Coursera under
Artificial Intelligence and Machine Leanrning in Amsterdam Tech University.

This is not a mandatory subject.

The following is the query ' Film_Locations_in_San_Francisco_20240513 ' structure 

'''
Films(
Title:              titles of the films, 
ReleaseYear:        time of public release of the films, 
Locations:          locations of San Francisco where the films were shot, 
FunFacts:           funny facts about the filming locations, 
ProductionCompany:  companies who produced the films, 
Distributor:        companies who distributed the films, 
Director:           people who directed the films, 
Writer:             people who wrote the films, 
Actor1:             person 1 who acted in the films, 
Actor2:             person 2 who acted in the films, 
Actor3:             person 3 who acted in the films
)		
'''

I will now follow the exercise given by coursera and afterwards try to play with pandas,
see what I can learn from it.

How to use:
Download the CSV file and run the Python code to create a .db (database) file,
secondly open the .db file with SQL, once this steps are completed you can easily manipulate the data using SQL.

Here are some commands in SQL you can run to retrieve the data:

 SELECT * FROM Fimls;
 SELECT Title, ReleaseYear FROM Fimls;
 SELECT Title, ProductionCompany, ReleaseYear FROM Films WHERE Writer IS 'James Cameron';
 SELECT Title, Actor1, ReleaseYear FROM Films WHERE ReleaseYear>=2015;


Alternatively you can update the Python code accondingly to your need. 