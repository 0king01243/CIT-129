from bs4 import BeautifulSoup
import requests

'''
file = open('C:/Users/Telepie/Documents/Web/apiwebsite.html')
html = file.read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.head.meta)
l = soup.findAll(class_='subtitle')
for item in l:
    print(item.text)
'''

'''
url = 'http://www2.county.allegheny.pa.us/RealEstate/GeneralInfo.aspx?ParcelID=0161N00212000000&' \
      'SearchType=2&SearchStreet=Lincoln&SearchNum=202&SearchMuni=803'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
element = soup.find('span', id='BasicInfo1_lblOwner')
print(element.text)
'''


url = 'https://pokemondb.net/pokedex/national'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
element = soup.findAll(class_='infocard-lg-data text-muted')
names = soup.findAll(class_='ent-name')
type = input("What type of pokemon would you like to search for?")
pokemon_types = soup.findAll(class_ = 'itype ' + type.lower())

'''
data = {}
y = -1
for x in element:
    y += 1
    data.update({y: x})
for x in data:
    print(data[x].find('small').text)
'''

counter = -1
for x in element:
    counter += 1
    if type in x.text:
        p = x.parent
        for child in p.children:
            print(child.text)
        #print(names[counter].text)
        #print(pokemon_types[counter].text)

