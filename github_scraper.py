import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')
url = f'https://github.com/{github_user}'
r = requests.get(url)
soup = bs(r.content, 'html.parser')

profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print(f'Profile Image Link: {profile_image}')

full_name = soup.find('span', {'itemprop' : 'name'}).text.strip()
print(f'Full Name: {full_name}')

location = soup.find('span', {'class' :'p-label'}).text
print(f'And They Live In: {location}')