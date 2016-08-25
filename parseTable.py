import urllib
from bs4 import BeautifulSoup


response_1 = urllib.urlopen('https://www.sec.gov/Archives/edgar/data/909661/000090966106000059/0000909661-06-000059.txt').read()
parse_1 = BeautifulSoup(response_1)

strTable = []
for id,line in enumerate(parse_1.find('table')):
    if id == 1: strTable = str(line);

for line in strTable.split('\n')[5:]:
    lineOut = ''
    for line_2 in line.split():
        if ' ' in line_2 : continue
        lineOut = lineOut + ' ' + line_2
    print lineOut
