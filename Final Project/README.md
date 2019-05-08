# DAT-129
## Pokemon Website Scraping

Took pokemon name, id, type, and effectiviness from a [pokemon database][idx] and made a text file of the id, name, and type with json,  html, beautiful soup, requests, and regular expressions so others may use the data for their own purposes. The website and program can also be used to find out a variety of different things about pokemon and list them out in an easy format for people to understand. 

## Complications

There were many aspects of the website that we wished to scrape but unfortunately some of the data was difficult to obtain due to the new mechanics added to the later generation of games. For example: 

![Image of Charizard](Charizard.PNG)
![Mega Charizard](MegaCharizard.PNG)

Pokemon that have mega-evolutions used some of the tags that we were previously calling and made it difficult for us to get information on items such as ability.

Make sure to use the file named "final_pokemon.py" to access the program
## Ideas for development
The next step in this development would be to gain more battle pertinent information such as IV's types, mega evolutions, or maybe recommended items.  The primary obstacle to doing this would be to standardize this accross all pokemon, as some have many more abilites/evolutions than others.  If this would be achievable, this would be more useful for the user.


[idx]:https://pokemondb.net/pokedex/national
