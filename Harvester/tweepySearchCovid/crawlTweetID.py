# https://github.com/thepanacealab/covid19_twitter/blob/master/dailies/2022-01-01/2022-01-01-dataset.tsv.gz
import requests
import datetime
import pandas as pd

def saveFile(givenTime):
    urlGenerate = "https://github.com/thepanacealab/covid19_twitter/raw/master/dailies/" + givenTime + "/" + givenTime + "_clean-dataset.tsv.gz"
    r = requests.get(urlGenerate)
    open("covidTweetID/" + givenTime + ".tsv.gz", "wb").write(r.content)

start = datetime.datetime.strptime("09-04-2022", "%d-%m-%Y")
date_generated = pd.date_range(start, periods=1)
date_range = date_generated.strftime("%Y-%m-%d")

# save tweetID file
for date in date_range:
    saveFile(date)
