from unittest import TestCase, main

import webarchives

class TestLookup(TestCase):

    def test_lookup(self):
        results = webarchives.lookup("http://nytimes.com")
        self.assertTrue(len(results) > 0)

    def test_internet_archive(self):
        results = webarchives.internet_archive.lookup('http://nytimes.com')
        self.assertTrue(len(results) > 0)

    def test_british_library(self):
        results = webarchives.british_library.lookup('http://bbc.co.uk')
        self.assertTrue(len(results) > 0)

    def test_archiefweb(self):
        results = webarchives.archiefweb.lookup('http://www.denhelder.nl/')
        self.assertTrue(len(results) > 0)

if __name__ == "__main__":
    main()
