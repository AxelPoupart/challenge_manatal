import requests
import re
from bs4 import BeautifulSoup

url = 'https://twitter.com/KMbappe'


def scrapping_twitter_followers(url):

    # Request the page
    request_exec = requests.get(url)
    result_content = request_exec._content

    # I first write it on a page to see what it look like
    # f = open("exercice_4/page.html", "w+")
    # f.write(html_doc.decode("utf-8"))
    # f.close()

    # Use beautifulSoup
    soup = BeautifulSoup(result_content, features="html.parser")

    # Find the right place
    flag = False
    for span in soup.find_all('span'):
        if span.string == 'Follower':
            # print(span.string) # Should print 'Follower'
            flag = True
        elif flag:
            follower_count = span.get("data-count")
            flag = False

    return follower_count


print(scrapping_twitter_followers(url))
