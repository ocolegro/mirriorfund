import urllib
from bs4 import BeautifulSoup
import commands,json

def cusipToTicker(cusip):
    '''
    url = r"""curl 'http://www.isincodes.net/action/s.php' -H 'Cookie: __atuvc=3%7C34; __atuvs=57bfba884ce30673000; __atssc=google%3B3; _ga=GA1.2.165094089.1472084159; _gat=1' -H 'Origin: http://www.isincodes.net' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://www.isincodes.net/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'search=""" + cusip + """' --compressed"""
    status,output = commands.getstatusoutput(url)
    '''
    url = r"""curl -sS 'http://quotes.fidelity.com/mmnet/SymLookup.phtml?reqforlookup=REQUESTFORLOOKUP&productid=mmnet&isLoggedIn=mmnet&rows=50&for=stock&by=cusip&criteria=""" + cusip + r"""&submit=Search' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Referer: http://quotes.fidelity.com/mmnet/SymLookup.phtml?reqforlookup=REQUESTFORLOOKUP&productid=mmnet&isLoggedIn=mmnet&rows=50&for=stock&by=D&criteria=101137107&submit=Search' -H 'Cookie: v1st=4EE0F5A8E6C6F24F; WRUID=307478319.1057844998; MC=uERop07erjnNpJIjDAFskz_L^f8SAle^OIQKAiklIABuwgADqjMGBAAKADIGBVe^PQ8AAAAAAAAAAAAAAAAAP03; cvi=p1=57be38840a02292520006ec20003aa33&p2=&p3=99&p4=&p5=&p6=&p7=57be38840a02292520006ec20003aa33&p8=; s_pers=%20visitStart%3D1472084144035%7C1503620144035%3B%20gpv_c11%3DFid.com%2520web%257Cresearch%257Cfixed%2520income%257CFind%2520Bonds%2520and%2520CDs%7C1472087404136%3B; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B; s_vi=[CS]v1|2BDF1C5805010B85-400001494000157D[CE]; __CT_Data=gpv=5&apv_178_www12=3&cpv_178_www12=3&rpv_178_www12=3' -H 'Connection: keep-alive' --compressed"""
    status,output = commands.getstatusoutput(url)
    #print output
    parse_2 = BeautifulSoup(output).find_all("a")
    returnTicker = ''
    for line in parse_2:
        if "SID_VALUE_ID" in str(line):
            returnTicker =  str(line).split("</a>")[0].split(">")[1]
    return returnTicker

