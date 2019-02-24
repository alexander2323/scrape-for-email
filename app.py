import re
import requests
from bs4 import BeautifulSoup

url = "http://byggomontageservice.se/kontakt/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser');

if soup.select("a[href*=mailto]"):
    email = str(soup.select("a[href*=mailto]")[0])
    print (email[email.find('mailto:')+len('mailto:'):email.rfind('"')])
else:
    print ("no mailto")