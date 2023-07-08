
#! Profile Twitter → @Tutialfred

import requests
from bs4 import BeautifulSoup





url = "https://alfredozavala.netlify.app/"
url = "https://twitter.com"

response = requests.get(url)





soup = BeautifulSoup(response.content, 'html.parser')

page_name = soup.find('span', class_='ProfileHeaderCard-nameLink u-textInheritColor js-nav').text
print(page_name)



