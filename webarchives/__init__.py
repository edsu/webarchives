import webarchives.backends

def lookup(url):
    # TODO: lookup in all the backends in parallel
    return backends.internet_archive.lookup(url)
