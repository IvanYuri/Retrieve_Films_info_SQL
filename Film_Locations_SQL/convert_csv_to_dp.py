import sqlite3
import pandas as pd

# This is a func that converts data retrieved from https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am/about_data
def converter():
    # this line creates the db file if not exist
    conn = sqlite3.connect('FilmsLocations.db')

    # this line opens the csv using pandas
    df = pd.read_csv('Film_Locations_in_San_Francisco_.csv')

    # this line converts csv to database(db)
    df.to_sql('Films', conn, if_exists='replace', index=False)

    # create a cursor object to manipulate the data
    cur = conn.cursor()

    # fetch and display data for testing purposes
    for row in cur.execute('SELECT * FROM Films'):
        print(row)
        
    # close connection
    conn.close()

# call the function
converter()
