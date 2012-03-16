import urllib
import StringIO
from lxml import etree
from dateutil import parser as dateparser

parser = etree.HTMLParser()
baseuri = "http://enterprise.archiefweb.eu/archives/archiefweb/"
staruri = baseuri + "*/"

def lookup(request_url):

    iauri = staruri + request_url

    fh = urllib.urlopen(iauri)
    data = fh.read()
    fh.close()

    dom = etree.parse(StringIO.StringIO(data), parser)

    alist = dom.xpath('//td[@class="mainBody"]/a')
    changes = []

    for a in alist:
        if a.attrib.has_key('name'):
            continue

        # XXX pull out of link
        try:
            dtobj = dateparser.parse(a.text + " 00:00:00 GMT")
        except:
            raise ValueError(a.text)
        loc = a.attrib['href']
        info = {'last' : dtobj, 'obs': 1}
        changes.append((dtobj, loc, info))

    return changes
