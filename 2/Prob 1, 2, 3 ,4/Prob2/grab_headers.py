'''
Created on Mar 5, 2017

@author: Denis
'''

import urllib.request
import re

search = input("What to search for: ")

url = 'https://duckduckgo.com/html?'
values = {'q': search,
          't': 'h_',
          'ia': 'me'}

# regex to search for headings
regex = re.compile(("<h\d.*?</h\d>"), re.DOTALL)


def read():
    """
    Grabs all the headings from an search query from duckduckgo.com/html
    """
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)  # requst the url to open
    respData = resp.read().decode()     # get all the html code
    for email in re.findall(regex, respData):   # search for all the headings
        print(email)

read()
