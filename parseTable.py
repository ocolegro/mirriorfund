import urllib
from bs4 import BeautifulSoup
import util as u

response_1 = urllib.urlopen('https://www.sec.gov/Archives/edgar/data/909661/000090966106000059/0000909661-06-000059.txt').read()
parse_1 = BeautifulSoup(response_1)

for id,line in enumerate(parse_1.find('sec-header')):
    if id == 0:
        date = str(line).split('\n')[0].split(':')[1].strip()
date =  [date[0:4],date[4:6],date[6:8]]

strTable = []
for id,line in enumerate(parse_1.find('table')):
    if id == 1: strTable = str(line);

retArr = []
for id,line in enumerate(strTable.split('\n')[6:]):
    lineOut = ''
    if "</c>" in str(line): continue
    for line_2 in line.split():
        if ' ' in line_2 : continue
        lineOut = lineOut + ' ' + line_2
    #ticker = u.cusipToTicker(lineOut.split()[-7])
    #if ticker != '':
    retArr.append([u.cusipToTicker(lineOut.split()[-7]),float(lineOut.split()[-6].replace(',','')),float(lineOut.split()[-5].replace(',','')),lineOut.split()[-4]])
print date,retArr

