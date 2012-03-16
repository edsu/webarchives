webarchives
===========

webarchives is a Python module for easily determining if a given URL is 
available from a known Web archiving project. The idea is that it could be handy
in situations where you have a URL, but the URL no longer resolves, and you would like to see the content. Web archiving projects are being run by national 
libraries, archives and non-profits that are part of the 
[International Internet Preservation Consortium](http://www.netpreserve.org/).

The genesis for webarchives was work done by the [Memento
Project](http://www.mementoweb.org/) on the [Memento
Proxy](http://www.mementoweb.org/tools/proxy/) which provided the seed for the
scraping backend modules used by webarchives.

Usage
-----

The webarchives module provides a function `lookup`, which you pass a url that 
you want to lookup in the Web archives. `lookup` will return a list of 
`(time, url)` tuples. Each tuple represents when the requested url was 
archived and where the archived representation can be retrieved from.

```python

import webarchives

print webarchives.lookup("http://www.geocities.com/homestead/homedir.html")
```

