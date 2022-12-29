from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page= requests.get(START_URL)
Soup=BeautifulSoup(page.text,"html.parser")
star_table=Soup.find("table")
templist=[]
tablerows=star_table.find_all("tr")
for tr in tablerows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    templist.append(row)

star_name=[]
distance=[]
mass=[]
radius=[]
lum=[]
for i in range(1,len(templist)):
    star_name.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    lum.append(templist[i][7])

df2=pd.DataFrame(list(zip(star_name,distance,mass,radius,lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
df2.to_csv("bright_stars.csv")