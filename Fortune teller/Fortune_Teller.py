"""
Created by Author: Rishikesh 'Richie' Maddi on Revision date: 2/09/19.
Email: rreddy67@gmail.com, rmadd2@unh.newhaven.edu
Program Summary: MadLibs Fortune Teller  .
Copyright Â© 2019 Richie. All rights reserved.
"""

import random


def output_file(word):
    output = open("fortune.txt", "w+")
    output.write(word)
    output.close()


def get_teller(user_selection):
    fortune = open("input.txt", "r")
    lines = fortune.read()
    sentence = lines.split('.')
    selection = int(user_selection)
    word = sentence[selection].split()
    if selection == 0:
        adj = get_words(selection)
        word = sentence[selection].replace('[Adjective]', adj)
        output_file(word)
    if selection == 1:
        noun = get_words(selection)
        word = sentence[selection].replace('[Noun]', noun)
        output_file(word)
    if selection == 2:
        plural_noun, game = get_words(selection)
        word = sentence[selection].replace('[Plural Noun]', plural_noun).replace("[Game]", game)
        output_file(word)
    if selection == 3:
        verb = get_words(selection)
        word = sentence[selection].replace("[Verb ending in'ing']", verb)
        output_file(word)
    if selection == 4:
        plural_noun, verb = get_words(selection)
        word = sentence[selection].replace('[Plural Noun]', plural_noun).replace("[Verb ending in'ing']", verb)
        output_file(word)
    if selection == 5:
        noun, plant, part = get_words(selection)
        word = sentence[selection].replace('[Noun]', noun).replace("[Plant]", plant).replace("[Part of body]", part)
        output_file(word)
    if selection == 6:
        place, verb = get_words(selection)
        word = sentence[selection].replace('Place]', place).replace("[Verb ending in'ing']", verb)
        output_file(word)
    if selection == 7:
        adj, number, plural_noun = get_words(selection)
        word = sentence[selection].replace('[Adjective]', adj).replace('[Number]', number)\
            .replace('[Plural Noun]', plural_noun)
        output_file(word)
    return word


def get_words(user_selection):
    if user_selection == 0:
        adjective = input('\tEnter an adjective: ')
        return adjective
    elif user_selection == 1:
        noun = input('\tEnter a Noun: ')
        return noun
    elif user_selection == 2:
        plural_noun = input('\tEnter a PluralNoun : ')
        game = input("\tEnter a game:")
        return plural_noun, game
    elif user_selection == 3:
        verb = input("\tEnter a verb ending with 'ing' ")
        return verb
    elif user_selection == 4:
        plural_noun = input('\tEnter a Plural Noun :')
        verb = input("\tEnter a verb ending with 'ing' :")
        return plural_noun, verb
    elif user_selection == 5:
        noun = input('\tEnter a Noun :')
        plant = input('\tEnter the name of plant :')
        body = input('\tEnter a part of body :')
        return noun, plant, body
    elif user_selection == 6:
        place = input('\tEnter the name of a place you want to visit :')
        verb = input("\tEnter a verb ending with 'ing' :")
        return place, verb
    elif user_selection == 7:
        adjective = input('\tEnter an adjective :')
        number = input('\tEnter a number :')
        plural_noun = input('\tEnter a Plural Noun :')
        return adjective, number, plural_noun


while True:
    print("\t+++++++++++++++WELCOME TO DIGITAL FORTUNE TELLER+++++++++++++++\t\n")

    print('\t 1. Select option 1 to Quit the game \n')
    print('\t 2. Select option 2 to start the game \n')

    option1 = input('\t Please enter your option: ')
    if option1 == '1':
        exit("\t\tThank you for playing\t\t")

    print("\nPlease select one of the following colors: ")
    print("\n\tRed")
    print("\n\tBlue")
    print("\n\tGreen")
    print("\n\tPurple")

    option2 = input('\n Please enter your color:\t')
    if option2 == 'Red' or 'red' or 'blue' or 'Blue' or 'Green' or 'Green' or 'Purple' or 'purple':
        start = random.randint(1, 2)
        if start == 1:
            user_choice = input("select from one of the following numbers  0 , 3 , 4 , 7 : \t")
            get_teller(user_choice)
            again = input('\nPlease select 1 to play again: ')
            if again != '1':
                print('\n------------------Thank you for playing---------------------\n')
                break

        elif start == 2:
            user_choice = input(" select from one of the following numbers  1 , 2 , 5 , 6 : \t")
            get_teller(user_choice)
            again = input('\nPlease select 1 to play again: ')
            if again != '1':
                print('\n------------------Thank you for playing------------------------\n')
                break

    else:
        print('\t\tSelect a proper color :\n')
