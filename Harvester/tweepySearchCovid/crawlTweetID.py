# https://github.com/thepanacealab/covid19_twitter/blob/master/dailies/2022-01-01/2022-01-01-dataset.tsv.gz
import requests
import datetime
import pandas as pd
import os, gzip, shutil


def saveFile(givenTime):
    urlGenerate = "https://github.com/thepanacealab/covid19_twitter/raw/master/dailies/" + givenTime + "/" + givenTime + "_clean-dataset.tsv.gz"
    r = requests.get(urlGenerate)
    open("covidTweetID/" + givenTime + ".tsv.gz", "wb").write(r.content)


dir_name = 'x'


def gz_extract(directory):
    extension = ".gz"
    curPath = os.path.abspath(os.getcwd())
    os.chdir(curPath + "\\" + directory)
    for item in os.listdir(curPath + "\\" + directory):  # loop through items in dir
        if item.endswith(extension):  # check for ".gz" extension
            gz_name = os.path.abspath(item)  # get full path of files
            file_name = (os.path.basename(gz_name)).rsplit('.', 1)[0]  # get file name for file within
            with gzip.open(gz_name, "rb") as f_in, open(file_name, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
            os.remove(gz_name)  # delete zipped file


start = datetime.datetime.strptime("01-01-2022", "%d-%m-%Y")
end = datetime.datetime.strptime("09-04-2022", "%d-%m-%Y")
date_generated = pd.date_range(start, end)
date_range = date_generated.strftime("%Y-%m-%d")

# save tweetID file
# for date in date_range:
#     saveFile(date)

# unzip all gz to a directory
dir_name = 'covidTweetID'
gz_extract(dir_name)
