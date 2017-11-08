from datetime import timedelta, date
import json
import gzip
import sys
import os
import time

start_time = time.time()
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

# Set the Date!
start_date = date(2012, 10, 1)
end_date = date(2013, 1, 1)

# Set the Hours of each day!
Hours = range(0,24)
for i in Hours:
    Hours[i] = str(i).zfill(2)

A = []
Date = []
for single_date in daterange(start_date, end_date):
    A = [single_date.strftime("%Y%m%d"),single_date.strftime("%Y-%m-%d")]
    Date.append(A)

Current_directory = os.getcwd()
print (Current_directory)
Total_Number_of_Tweets = 0

for dd in Date:
    Tweets = []
    table = []
    PIK = []
    Directory = Current_directory+"\\mehdi\\" + dd[0]
    os.chdir(Directory)
    for i in Hours:
        Hour = "tweets.txt." + dd[1] +"_"+str(i)+".gz"
        try:
            with gzip.open(Hour, 'r') as f:
                for line in f:
                    try:
                        j = line.split('|',1)[-1]
                        try:
                            Tweets = [json.loads(j)['text'],json.loads(j)['coordinates']['coordinates'],json.loads(j)['created_at'],json.loads(j)['user']['screen_name']]
                            table.append(Tweets)
                        except TypeError:
                            continue
                    except ValueError:
                        # Probably there is a bad JSON
                        continue
        except:
            print "This hour is not available!  :", Hour
            continue
    os.chdir(Current_directory+"\\Collapsed")
    print "Number of Tweets of this day",dd[1],"is",(len(table))
    Total_Number_of_Tweets = Total_Number_of_Tweets + len(table)
    PIK = "tweets.txt." + dd[1] + ".json" + ".gz"
    with gzip.open(PIK, "wb") as ff:
        for Tweet in table:
            json.dump(Tweet, ff)
            ff.write('\n')
    ff.close()


print "Total Number of Tweets:", Total_Number_of_Tweets
print("--- %s seconds ---" % (time.time() - start_time))

