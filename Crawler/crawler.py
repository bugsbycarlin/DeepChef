"""

  crawler.py
  Matthew Carlin
  November 2017

  A crawler built to process pages from www.openeats.org to generate training data for DeepChef

"""

import BeautifulSoup
import time
import urllib
import urllib2
import urlparse


import page_processor

CRAWL_LIMIT = 100000000
SLEEP_TIME = 0.15
SEED_URL = "http://www.openeats.org"

blacklist_elements = [
  "tags/",
  "profiles/",
  "follow/",
  "accounts/",
  "export/"
]

def crawl(seed_url, domain, crawl_limit, sleep_time):
  to_crawl = [seed_url]
  crawled = []
  while to_crawl and len(crawled) < crawl_limit:
    url = to_crawl.pop()
    if url not in crawled:
      print "Crawling " + url
      print "Length of crawl queue is %d." % len(to_crawl)
      print "Total crawled so far is %d." % len(crawled)
      try:
        page_source = retrieve(url)

        links = getLinks(page_source, url, domain)

        if "recipe/" in url:
          page_processor.process(url, page_source)

        for link_url in links:
          to_crawl.append(link_url)
      except urllib2.URLError, e:
        print "Encountered URLError"
        print e

      crawled.append(url)

      time.sleep(sleep_time)

def retrieve(url):
  page_source = urllib2.urlopen(url).read()
  return page_source


def getLinks(page_source, url, domain):
  """Return a list of links obtained from the page.

  Restrict to urls which match the domain name, and relative urls with
  the domain name correctly attached."""
  try:
    soup = BeautifulSoup.BeautifulSoup(page_source)
    raw_links = soup.findAll('a', href=True)

    links = []
     
    for raw_link in raw_links:
      link = raw_link['href']

      blacklist = False
      for blacklist_element in blacklist_elements:
        if blacklist_element in link:
          blacklist = True
      if blacklist:
        continue
            
      if domain in link:
        links.append(link)
      elif "http" in link: # skip offsite links
        continue
      elif link[0] == "/":
        link = domain + link
        links.append(link)
      elif link[0:2] == "./" or link[0:3] == "../":
        link = urlparse.urljoin(url, link)
        links.append(link)
      else:
        link = urlparse.urljoin(url, link)
        links.append(link)

    return links
  except:
    return []

#test_url = "http://www.openeats.org/recipe/jamaican-goat-curry/"
#test_url = "http://www.openeats.org/recipe/golden-rum-cake/"
#test_url = "http://www.openeats.org/recipe/chesty-chicken/"
#test_url = "http://www.openeats.org/recipe/garlic-mash-taters/"
#crawl(test_url, SEED_URL, CRAWL_LIMIT, SLEEP_TIME)

crawl(SEED_URL, SEED_URL, CRAWL_LIMIT, SLEEP_TIME)

