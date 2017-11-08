import json
import gzip
import csv
import string
import re

Filtered_Tweets = []
j = 0

#Disaster related words --- All characters must be in "Lower case" ---
Financial = ["insurance", "money", "budget", "loan","finance","financial", "#insurance", "#money", "#budget", "#loan","#finance","#financial"]
Infrastructure = ["electricity", "power", "outage", "facility","transportation", "#electricity", "#power", "#outage", "#facility","#transportation"]
Housing = ["shelter", "dwelling", "residence", "house","home", "#shelter", "#dwelling", "#residence", "#house","#home"]
Family = ["family", "children","daughter","husband","wife", "#family", "#children", "#son", "#daughter","#husband","#wife"]
Community = ["community", "people", "neighbors", "neighbor","neighborhood","society", "#community", "#people", "#neighbors", "#neighbor","#neighborhood","#society"]

# List of topics:
Topics = ["Financial","Infrastructure","Housing","Family","Community"]

# List of list of topics:
List_of_lists_topics = []
for topic in Topics:
    List_of_lists_topics.append(eval(topic))

# Flattened list of topics:
Flattened_list_of_topics = [val for sublist in List_of_lists_topics for val in sublist]

# Define regular expression for removing punctuations except Hashtag '#'
remove = string.punctuation
remove = remove.replace("#", "") # don't remove hashtag
pattern = r"[{}]".format(remove) # create the pattern


PIK1 = "Dis_Exp_GEOID_Winner/" + "Dis_Exp_GEOID_Winner.json" + ".gz"
PIK2 = "Dis_Exp_Topic_Identified/" + "Dis_Exp_Topic_Identified.json" + ".gz"

with gzip.open(PIK1, "rb") as ff:
    for line in ff:
        try:
            Tweet = json.loads(line)
            Text = Tweet[0]
            Text = re.sub(pattern, "", Text)
            Text = Text.lower()
            Text = Text.split(' ')
            if any(i in Text for i in Flattened_list_of_topics):
                j = j + 1
                for Topic in Topics:
                    if any(i in Text for i in eval(Topic)):
                        # Identified_Tweet = [Topic,Long = Tweet[1],Lat = Tweet[2],Date.index = Tweet[3],GEOID_Winner = Tweet[-1]]
                        Identified_Tweet = [Topic,Tweet[1],Tweet[2],Tweet[3],Tweet[-1]]
                        with gzip.open(PIK2, "a") as gg:
                            json.dump(Identified_Tweet, gg)
                            gg.write('\r\n')
                            
        except:
            continue

print j      
                    
                   