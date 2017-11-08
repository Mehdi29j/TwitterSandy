from datetime import timedelta, date
import time
import json
import gzip
import os

# Set the directory to "Located_tweets" folder
Current_directory = os.getcwd()
os.chdir(Current_directory+"\\Located_tweets")

PIK = "Selected_screen_names" + ".json" + ".gz"
with gzip.open(PIK, "rb") as ff:
   screen_names = json.load(ff)

print (len(screen_names))
print screen_names[10]

start_time = time.time()
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

# Set the Date!
start_date = date(2012, 10, 1)
end_date = date(2013, 1, 1)



#Create string for Dates
Date = []
for single_date in daterange(start_date, end_date):
    Date.append(single_date.strftime("%Y-%m-%d"))
    
print Date
i = 0
j = 0

# Start the loop over .json "collapsed" files
for dd in Date:
    i = 0
    print dd
    Disaster_Exp_Tweets = []
    os.chdir(Current_directory+"\\Collapsed")
    PIK = "tweets.txt." + dd + ".json" + ".gz"
    with gzip.open(PIK, "rb") as ff:
        for line in ff:
            Tweet = json.loads(line)
            Name = Tweet[-1]
            if Name in screen_names:
                Selected_Tweet = [Tweet[0],Tweet[1],Date.index(dd),Name]
                Disaster_Exp_Tweets.append(Selected_Tweet)
    ff.close()

    os.chdir(Current_directory+"\\Dis_Exp_Tweets")
    PIK = "Dis_Exp_All_Tweets" + ".json" + ".gz"
    with gzip.open(PIK, "a") as gg:
        for T in Disaster_Exp_Tweets:
            json.dump(T, gg)
            gg.write('\r\n')
            j = j + 1
            i = i + 1
    gg.close()
    print "Total number of Tweets of disaster experinced people and this day:  ", i

print "Total number of Tweets of disaster experinced people:  ",j            

