from bs4 import BeautifulSoup
import requests

data=requests.get('https://www.imdb.com/find?q=horror&ref_=nv_sr_sm')
soup=BeautifulSoup(data.content,'html.parser')
print(soup.prettify())

