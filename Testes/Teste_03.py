!pip install requests
!pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

url = "https://www.nasa.gov/"
response = requests.get(url)

if response.status_code == 200:

  soup = BeautifulSoup(response.text, "html.parser")

  links = soup.find_all('a')

  for link in links:
    print(link.get('href'))

else:
  print("Erro ao acessar a página:", response.status_code)

