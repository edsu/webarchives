import urllib
from lxml import etree
from dateutil import parser as dateparser

base = "http://wayback.archive.org/web/xmlquery?url=%s&startdate=1996"

def lookup(request_url):
    url = base % request_url
    fh = urllib.urlopen(url)

    data = fh.read()
    fh.close()

    dom = etree.XML(data)
    changes = []

    rlist = dom.xpath('//result')
    for a in rlist:

        dtstr = (a.xpath("./capturedate"))[0].text
        loc = "http://web.archive.org/web/%s/%s" % (dtstr, (a.xpath("./url"))[0].text)
        dtstr += " GMT"
        dtobj = dateparser.parse(dtstr)
        if changes and changes[-1][0] == changes[-1][2]['last']:
            changes[-1][2]['last'] = dtobj
        if a.tail:
            changes.append((dtobj, loc, {'last' : dtobj, 'obs' : 1, 'type' : 'observed'}))
        else:
            changes[-1][-1]['last'] = dtobj
            changes[-1][-1]['obs'] += 1

    changes.sort()
    return changes
