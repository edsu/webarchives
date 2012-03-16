import internet_archive, archiefweb, british_library, canada

def lookup(url):
    # TODO: lookup in all the backends in parallel
    return internet_archive.lookup(url)
