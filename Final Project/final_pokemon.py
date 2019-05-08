from bs4 import BeautifulSoup
import requests
import re
import json

# This block of code is the standard way to access a url, then use HTML to parse it.
url = 'https://pokemondb.net/pokedex/national'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
element = soup.findAll(class_='ent-name')


# This dictionary was created to be filled completely with all pokemon data
pokemon = {"id": [], "name": [], "type": []}

# Because pokemon entry numbers go from 1 - 808, as it finds each name, we store an id as the
# number of calls it has had to make.  We determine this number by the variable place.
place = 0
for items in element:
    pokemon['name'].append(items.text)
    place += 1
    pokemon['id'].append(place)

# Because some pokemon have more than one type, we cannot just store all of them into a list
# and assign that to a pokemon name.  We used Regular Expressions in order to a list of all
# types, then found their parents and stored them in the dictionary daddy.
daddy = {}
regex = re.compile('itype ([a-zA-Z]+)')
element2 = soup.findAll(class_=regex)

for x in range(0,len(element2)):
    daddy[x] = element2[x].find_parent("small").previous_sibling.previous_sibling

# This loop was used to determine if two pokemon had the same dad, and if they did, they were stored
# as one string together in our type list.
for x in range(0, len(daddy)-1):
    if daddy[x] == "checked":
        pass
    elif daddy[x] == daddy[x+1]:
        pokemon['type'].append((element2[x].text, element2[x + 1].text))
        daddy[x + 1] = "checked"
    else:
        pokemon['type'].append([element2[x].text])

# Unfortunately, this loop did not allow us to capture the last item in the list's type, which had to be entered manually.
# We achieved this by having it copy the previous pokemon's type, which was shared.
pokemon['type'].append(pokemon['type'][-1])
# This code block exports all of the pokemon data into a text file
file_name = "pokemon.txt"
with open(file_name, "w+") as f:
    f.write(json.dumps(pokemon))
# These following dictionary and list were set up for a few reasons.
# The type effectiveness dictionary shows every potential way that a pokemon attact can affect its opponent.
# We will later be filling all of these with values determined in the weakness checker.
type_effectiveness = {"1/2 Effective": [], "1/4 Effective": [], "No Effect": [], "Normal Effective": [], "Double Effective": [], "Quadruple Effective": []}
# This list was created when we discovered that the list of pokemon types was not tagged and we had no clear way of calling it
list_of_types = ["Normal","Fire","Water","Electric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon"
                 ,"Dark","Steel","Fairy"]

# this function was originally created when we planned on using it more than once in our while loop below
# but it is still useful outside for clarity's sake
def weakness_checker(name):
    individual_url = "https://pokemondb.net/pokedex/" + name
    individual_request = requests.get(individual_url)
    individual_soup = BeautifulSoup(individual_request.text,'html.parser')
    regular_expression = re.compile("type-fx-cell type-fx-(\d)+")
    individual_weaknesses = individual_soup.findAll(class_=regular_expression)
# The reason that we cut the list down is for some pokemon entries that have multiple different type configurations
# For example, some pokemon have the ability to transform, so they list each of their weaknesses in their different forms
# This means that our function assumes that they will be in base form, but unfortunately this is the only way that we can do this
    individual_weaknesses = individual_weaknesses[:len(list_of_types)]
    type_counter = 0
# The list of all pokemon resistances are in the same order from every page
# So when we check the first item in the list of weaknesses, we know that it will always
# Be the first item in our list of types
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
            type_effectiveness["Normal Effective"].append(list_of_types[type_counter])
        type_counter += 1
# This block of code is used to print out all of the effectiveness results
    effectiveness_counter = 0
    for key in type_effectiveness:
        print("             " + list(type_effectiveness.keys())[effectiveness_counter], end=": ")
        if len(type_effectiveness[key]) == 0:
            print("None", end=" ")
        else:
            for value in type_effectiveness[key]:
                print(value, end=" ")
        print("     ")
        effectiveness_counter += 1


# This while loop is the main body of our code, which allows the user to search through for a pokemon either by id number or name
def main():
    while True:
        criteria = input("Would you like to search for a pokemon by name or id, or quit?  ")
        if criteria == "quit":
            quit()
        if criteria == "id" or criteria == "name":
            pass
        else:
            print("Please input either name, id, or quit")
            continue
        identification = input("Please insert the " + criteria + " of the pokemon you are looking for:  ")
        found = "no"
        for x in range(0, len(pokemon[criteria])):
            if str(pokemon[criteria][x]) == str(identification):
                print("Name: " + pokemon['name'][x].capitalize())
                # We chose to format the id number like this to be more traditional to the game
                # In the game, ids are listed with 0's filling up the blank positions to the hundreds
                # ex) 001, 011, 111
                if len(str(pokemon['id'][x])) == 1:
                    print("Id: 00{}".format(pokemon['id'][x]))
                elif len(str(pokemon['id'][x])) == 2:
                    print("Id: 0{}".format(pokemon['id'][x]))
                else:
                    print("Id: {}".format(pokemon['id'][x]))
                if len(pokemon['type'][x]) == 1:
                    print("Type: " + str(pokemon['type'][x])[2:][:-2])
                else:
                    print("Types: " + pokemon['type'][x][0] + ", " + pokemon['type'][x][1])
                print("Type Matchups:", end="\n")
                weakness_checker(pokemon['name'][x])
                global type_effectiveness
                type_effectiveness = {"1/2 Effective": [], "1/4 Effective": [], "No Effect": [], "Normal Effective": [], "Double Effective": [], "Quadruple Effective": []}
                print("", end="\n\n\n")
                found = "yes"
        if found == "yes":
            main()
        else:
          print("We did not find that pokemon in our database, please try again")


main()
