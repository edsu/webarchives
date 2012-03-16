import urllib
import StringIO
from lxml import etree
from dateutil import parser as dateparser

base = "http://www.collectionscanada.gc.ca/webarchives/*/"

def lookup(request_url):
    parser = etree.HTMLParser()

    url = base + request_url

    fh = urllib.urlopen(iauri)
    data = fh.read()
    fh.close()
    dom = etree.parse(StringIO.StringIO(data), parser)

    alist = dom.xpath('//div[@class="inner-content"]//a')
    changes = []

    for a in alist:
        if a.attrib.has_key('name'):
            continue
        dtobj = dateparser.parse(a.text + " 00:00:00 GMT")
        loc = a.attrib['href']
        info = {'last' : dtobj, 'obs': 1}
        changes.append((dtobj, loc, info))
    return changes
