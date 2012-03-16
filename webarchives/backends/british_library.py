import urllib
from lxml import etree
from dateutil import parser as dateparser

base = "http://www.webarchive.org.uk/wayback/archive/*/"

def lookup(request_url):

    url = base + request_url
    fh = urllib.urlopen(url)

    data = fh.read()
    fh.close()

    dom = etree.XML(data)
    changes = []

    rlist = dom.xpath('/wayback/results/result')
    for a in rlist:

        dtstr = a.xpath('./capturedate/text()')[0]
        url = a.xpath('./url/text()')[0]
        loc = "http://www.webarchive.org.uk/wayback/archive/%s/%s" % (dtstr, url)

        dtstr += " GMT"
        dtobj = dateparser.parse(dtstr)
        changes.append((dtobj, loc, {'last': dtobj, 'obs' : 1}))

    return changes
