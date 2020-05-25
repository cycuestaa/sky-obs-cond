# by cycuestaa
import os
import requests
import urllib.request
import time
import math
from bs4 import BeautifulSoup
from bs4 import CData

# set url to the website
url = 'https://www.cleardarksky.com/c/SmnCAkey.html'
response = requests.get(url)

# parse html
soup = BeautifulSoup(response.text, "html.parser")

# variables 
dest = "./res/"    # files save here. make sure ends with /
count = 1 
count_d = 1
clouds = []
trans = []
seeing = []
darkness = []
wind = []
humid = []
temp = []
date = ''
time = ''
max_time = ''

# GET Now's Date (6) & Time (7)
pc = 1
lc = 0
for p_tag in soup.findAll('p'):
    if pc == 60:
        ls = p_tag.text.split()
        for l in ls:
            if lc == 6:
                date = l
            elif lc == 7:
                time = l
                print("Today: ", date, time)
            lc += 1
    pc += 1


## Get what type of data 
query = input("Can only query 46 hours ahead: date & time (mm/dd/year 00:00:00): ")
print("Select which conditions matter (-a, -c, -d, -t, -s, -w, -h, -tm)")
print("All, Cloud Cover, Darkness, Transparency, Seeing, Wind, Humid, Temperature")
conds = input("Enter: ")
print(conds)

## CREATE directory, if doesnt exist
path = os.getcwd()
#print("Detected working dir:%s" % path)
#try:
#    os.mkdir(dest)
#except OSError:
#    print ("CREATE failed. dir: %s likely exists" % path)
#else:
#    print ("CREATE done. files will save into dir: %s" % path)

def get_time(xs):
    x=xs.split(':')
    i = 0
    for s in xs:
        if i == 0:
           return s 
        i += 1
    return 0

# calculate max showing time
# number of 24hrs, last
# time_dd = 0
for a_tag in soup.findAll('area'):  #'a' tags are for links
    row = math.floor(count/46)
    title = a_tag['title']
    if count >= 1 : # line for first file listed
        if ("Limiting" in title):
            # Darnkness
            if count_d == 4:
                darkness = []
                count_d = 1
            else:
                count_d += 1
                darkness.append(title) 
        else:
            #day = "23:00" in title
            if row == 0 : # Cloud Cover
                clouds.append(title)
            elif row == 1 : # Transparency
                trans.append(title)
            elif row == 2: # Seeing
                seeing.append(title)
            elif row == 3: # Wind
                wind.append(title)
            elif row == 4: # Humid
                humid.append(title)
            elif row == 5: # Temp
                temp.append(title)
            count += 1





