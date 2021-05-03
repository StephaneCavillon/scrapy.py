# -*- coding: utf8 -*-

#l'objectif de l'exercice et d'afficher une phrase au hasard parmis les 2 du tableau/liste quotes
# quotes = [
#     "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
#     "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
# ]

# characters = [
#     "alvin et les Chipmunks", 
#     "Babar", 
#     "betty boop", 
#     "calimero", 
#     "casper", 
#     "le chat potté", 
#     "Kirikou"
# ]

user_answer = input("Tapez Entrer pour connnaitre une autre citation et B pour quitter le programme")

# importation du module random
import random

# importation du module de lecture Json
import json 

# extraction des valeurs des json
def read_values_from_json(path, key):
    # Create a new empty list
    values = []
    # open a json file with my objects
    with open(path+".json") as file:
        # load all the data contained in this file
        data = json.load(file)
        # add each item in my list
        for entry in data:
            values.append(entry[key])
    # return my completed list
    return values

# Création d'une fonction de nettoyage des phrases trouvées
def clean_strings(sentences):
    cleaned=[]
    for sentence in sentences:
        # nettoyage des espaces
        clean_sentence = sentence.strip()
        # ajout des phrases nettoyées au tableau
        cleaned.append(clean_sentence)
    return cleaned

#défnition de la fonction de choix d'une phrase
def get_random_stuff(array):
    rand_number = random.randint(0, len(array)-1)
    item = array[rand_number] #get associated stuff from an array
    return item     #show the stuff

# retourner une valeur aléatoire à partir d'un json
def random_value(src_path, key):    
    all_value = read_values_from_json(src_path, key)
    clean_values = clean_strings(all_value)
    return get_random_stuff(clean_values)

def random_quote():
    return random_value('quote', 'quote')

def random_character():
    return random_value('characters','characters')

def print_message():
    rand_quote = random_quote()
    rand_character = random_character()
    return ">>>{} a dit: {}".format(rand_character,rand_quote)


def main_loop():
    while True:
        print_message()
        message = ('Voulez-vous voir une autre citation ?'
        'Pour sortir du programme, tapez [B].')
        choice = input(message).upper()
        if choice == 'B':
            break       # stoppera la boucle

if __name__ == '__main__':
    main_loop()
    

#écriture d'un message avec les données récoltées aléatoirement
# def message():
#     # extraction d'un personnage
#     all_characters = read_values_from_json("characters")
#     character = get_random_stuff(all_characters)

#     # extraction d'une quote
#     all_quote = read_values_from_json("quote")
#     quote = get_random_stuff(all_quote)

#     # capitalize(quote)
#     return "{} a dit: {}".format(character,quote)


# interface avec l'utilisateur
# while user_answer != "B":
#     print(message())
#     user_answer = input("Tapez Entrer pour connnaitre une autre citation et B pour quitter le programme")

