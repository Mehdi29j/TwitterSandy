from datetime import timedelta, date
import json
import gzip
import os
import time
import csv
import string
import re

start_time = time.time()
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

# Set the Date!
start_date = date(2012, 10, 26)
end_date = date(2013, 1, 1)

#Create string for Dates
Date = []
for single_date in daterange(start_date, end_date):
    Date.append(single_date.strftime("%Y-%m-%d"))

# Check the created string of dates
print "Number of Days:", (len(Date))

# Set the directory to "Collapsed" folder
Current_directory = os.getcwd()

#Disaster related words --- All characters should be in "Lower case" ---
Disaster_dictionary = ["sandy", "hurricane", "storm", "#sandy", "#hurricanesandy", "#njsandy", "#masandy" ,"#stormde", "#sandydc", "#rigov"]
print (Disaster_dictionary)

# Define disaster related tweets:
AA = 0
CC = []
L = []
Disaster_related = []

# Define regular expression for removing punctuations except Hashtag '#'
remove = string.punctuation
remove = remove.replace("#", "") # don't remove hashtag
pattern = r"[{}]".format(remove) # create the pattern

# Start the loop over .json files
for dd in Date:
    Disaster_related = []
    os.chdir(Current_directory+"\\Collapsed")
    PIK = "tweets.txt." + dd + ".json" + ".gz"
    with gzip.open(PIK, "rb") as ff:
        for line in ff:
            Tweet = json.loads(line)
            Text = Tweet[0]
            Text = re.sub(pattern, "", Text)
            Text = Text.lower()
            Text = Text.split(' ')
            for Word in Text:
                if Word in Disaster_dictionary:
                    Disaster_related.append(Tweet)
                    break
    del ff
    BB = "Number of disaster related Tweets of this day:  "+str(dd)+"  is:  "+str(len(Disaster_related))
    print BB
    CC.append(BB)
    AA = AA + len(Disaster_related)
    # Create the output file
    os.chdir(Current_directory+"\\Related")
    PIK = "Disaster_related_tweets." + dd + ".json" + ".gz"
    with gzip.open(PIK, "wb") as gg:
        json.dump(Disaster_related, gg)

# Total number of disaster related Tweets:
print "Total number of disaster related tweets:", AA

# Create CSV File:
os.chdir(Current_directory)
csvfile = "Num_Related_TW"+".csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in CC:
        writer.writerow([val])

# Running time
print("--- %s seconds ---" % (time.time() - start_time))

