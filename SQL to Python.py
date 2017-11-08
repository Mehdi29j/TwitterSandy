import json
import gzip
import sys
import os
import time
import sqlite3

i = 0

# Get the current directory:
Current_directory = os.getcwd()

PIK = "Dis_Exp_GEOID_Winner/" + "Dis_Exp_GEOID_Winner.json" + ".gz"

# Start SQL "Table: Final" to JSON gzip
conn = sqlite3.connect('Tweets.sqlite')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
with gzip.open(PIK, "a") as ff:
    for row in (cur.execute("SELECT * FROM Final")): #select data
        json.dump(list(row), ff)
        ff.write('\r\n')        
        i = i + 1

cur.execute("DROP TABLE Final")
        
conn.close()
    
print i




#for row in (cur.execute('Text, Long,  Lat, Date, Screen_name, GEOID, GEOID_Winner')): #selects data

