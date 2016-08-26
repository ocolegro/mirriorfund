from bs4 import BeautifulSoup
import urllib
from pymongo import MongoClient

client = MongoClient()
db     = client['primer']

#db.penny_stocks.insert(dict)
CIK    = '0001037389'
url_1 = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=%s&owner=exclude&count=100&hidefilings=0' %(CIK)
response_1 = urllib.urlopen(url_1).read()
parse_1 = BeautifulSoup(response_1).find_all("a")


prefix = 'https://www.sec.gov'
for line in parse_1:
    sLine = str(line)
    if 'Archives' in sLine:
        url_2 = prefix + (sLine.replace("<a href=\"","")).replace("Documents</a>","").replace("id=\"documentsbutton\">","").replace("\"","").split()[0]
        response_2 = urllib.urlopen(url_2).read()
        parse_2 = BeautifulSoup(response_2).find_all("a")
        tmpUrl = ''
        for line_2 in parse_2:
            sLine_2 = str(line_2)
            if 'Archives' in sLine_2:
                tmpUrl =  (sLine_2.replace("<a href=\"","")).replace("Documents</a>","").replace("id=\"documentsbutton\">","").replace("\"","").split('>')[0].split()[0]
        url_3 =  prefix + tmpUrl
        response_3 = urllib.urlopen(url_3).read()
        print url_2
        parse_3 = BeautifulSoup(response_3).find('table')
        print parse_3


url = r"""curl 'http://quotes.fidelity.com/mmnet/SymLookup.phtml?reqforlookup=REQUESTFORLOOKUP&productid=mmnet&isLoggedIn=mmnet&rows=50&for=stock&by=cusip&criteria=950590109&submit=Search' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Referer: http://quotes.fidelity.com/mmnet/SymLookup.phtml?reqforlookup=REQUESTFORLOOKUP&productid=mmnet&isLoggedIn=mmnet&rows=50&for=stock&by=D&criteria=101137107&submit=Search' -H 'Cookie: v1st=4EE0F5A8E6C6F24F; WRUID=307478319.1057844998; MC=uERop07erjnNpJIjDAFskz_L^f8SAle^OIQKAiklIABuwgADqjMGBAAKADIGBVe^PQ8AAAAAAAAAAAAAAAAAP03; cvi=p1=57be38840a02292520006ec20003aa33&p2=&p3=99&p4=&p5=&p6=&p7=57be38840a02292520006ec20003aa33&p8=; s_pers=%20visitStart%3D1472084144035%7C1503620144035%3B%20gpv_c11%3DFid.com%2520web%257Cresearch%257Cfixed%2520income%257CFind%2520Bonds%2520and%2520CDs%7C1472087404136%3B; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B; s_vi=[CS]v1|2BDF1C5805010B85-400001494000157D[CE]; __CT_Data=gpv=5&apv_178_www12=3&cpv_178_www12=3&rpv_178_www12=3' -H 'Connection: keep-alive' --compressed"""

