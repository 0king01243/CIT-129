from bs4 import BeautifulSoup
import requests
import re

url = 'https://pokemondb.net/pokedex/national'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
element = soup.findAll(class_='ent-name')

pokemon = {"id": [], "name": [], "type": []}

place = 0
for items in element:
    pokemon['name'].append((items.text).lower())
    place += 1
    pokemon['id'].append(place)

daddy = {}
regex = re.compile('itype ([a-zA-Z]+)')
element2 = soup.findAll(class_=regex)

for x in range(0,len(element2)):
    daddy[x] = element2[x].find_parent("small").previous_sibling.previous_sibling
    print(daddy[x])

for x in range(0, len(daddy)-1):
    if daddy[x] == "checked":
        pass
    elif daddy[x] == daddy[x+1]:
        pokemon['type'].append((element2[x].text, element2[x + 1].text))
        daddy[x + 1] = "checked"
    else:
        pokemon['type'].append(element2[x].text)

pokemon['type'].append(pokemon['type'][-1])
print(pokemon['type'])



type_effectiveness = {"1/2 Effective": [], "1/4 Effective": [], "No Effect": [], "Neutral": [], "Double Effective": [], "Quadruple Effective": []}
list_of_types = ["Normal","Fire","Water","Electric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon"
                 ,"Dark","Steel","Fairy"]


def weakness_checker(name):
    individual_url = "https://pokemondb.net/pokedex/" + name
    individual_request = requests.get(individual_url)
    individual_soup = BeautifulSoup(individual_request.text,'html.parser')
    regular_expression = re.compile("type-fx-cell type-fx-(\d)+")
    individual_weaknesses = individual_soup.findAll(class_=regular_expression)
    type_counter = 0
    for item in individual_weaknesses:
        if item.text == "½":
            type_effectiveness["1/2 Effective"].append(list_of_types[type_counter])
        elif item.text == "¼":
            type_effectiveness["1/4 Effective"].append(list_of_types[type_counter])
        elif item.text == "2":
            type_effectiveness["Double Effective"].append(list_of_types[type_counter])
        elif item.text == "4":
            type_effectiveness["Quadruple Effective"].append(list_of_types[type_counter])
        elif item.text == "0":
            type_effectiveness["No Effect"].append(list_of_types[type_counter])
        else:
            type_effectiveness["Neutral"].append(list_of_types[type_counter])
        type_counter += 1

    effectiveness_counter = 0
    for key in type_effectiveness:
        print(list(type_effectiveness.keys())[effectiveness_counter], end=": ")
        if len(type_effectiveness[key]) == 0:
            print("None", end="")
        else:
            for value in type_effectiveness[key]:
                print(value, end=" ")
        print("")
        effectiveness_counter += 1


weakness_checker("bulbasaur")

# DO NOT DELETE

while True:
    criteria = input("Would you like to search for a pokemon by name, id, or type?  ")
    if criteria == "name":
        name = input("Please input a pokemon name:  ").lower()
        for x in range(0,len(pokemon['name'])):
            if pokemon['name'][x] == name:
                print("Name: " + pokemon['name'][x].capitalize())
                if len(str(pokemon['id'][x])) == 1:
                    print("Id: 00{}".format(pokemon['id'][x]))
                elif len(str(pokemon['id'][x])) == 2:
                    print("Id: 0{}".format(pokemon['id'][x]))
                else:
                    print("Id: {}".format(pokemon['id'][x]))
                if len(pokemon['type'][x]) == 1:
                    print("Type: " + pokemon['type'][x])
                else:
                    print("Types: " + pokemon['type'][x][0] + ", " + pokemon['type'][x][1])


