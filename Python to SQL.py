import json
import gzip
import sys
import os
import time
import sqlite3

    
# Start JSON to SQL DataBase
conn = sqlite3.connect('Tweets.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''

CREATE TABLE IF NOT EXISTS Tweet (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Text   TEXT,
    Long INTEGER,
    Lat INTEGER,
    Date INTEGER,
    Screen_name TEXT,
    GEOID INTEGER
);

''')


i = 0

#  Current directory!
Current_directory = os.getcwd()
os.chdir(Current_directory+"\\Dis_Exp_Located")

PIK = "Dis_Exp_Located_Tweets" + ".json" + ".gz"
with gzip.open(PIK, 'r') as f:
    for Line in f:
        entry = json.loads(Line)
        try:
            Text = entry[0];
        except:
            Text = Null;
        try:
            Long = entry[1][0];
        except:
            Long = 0;
        try:
            Lat = entry[1][1];
        except:
            Lat = 0;
        try:
            Date = entry[2];
        except:
            Date = 10;
        try:
            Screen_name = entry[3];
        except:
            Screen_name = Null;
        try:
            GEOID = entry[4];
        except:
            GEOID = 10;

        cur.execute('''INSERT OR IGNORE INTO Tweet (Text, Long, Lat, Date, Screen_name, GEOID) 
            VALUES ( ?, ?, ?, ?, ?, ?)''', (Text, Long, Lat, Date, Screen_name, GEOID))
            
        
        i = i + 1
        if i > 10000:
            conn.commit()
            i = 0
                          
       
conn.commit()



