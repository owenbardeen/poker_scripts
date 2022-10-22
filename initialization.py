# intialization methods
import random
positions = [["under the gun", "1", 1], ["hijack", "2", 2], ["cutoff", "3", 3], 
["button", "4", 4], ["small blind", "5", 5]]
def name(position):
    return position[0]
def index(position):
    return position[1]
def construct():
    cards = [
    #aces
    ["ace of hearts", 14, "spades"],
    ["two of hearts", 2, "hearts"],
    ["three of hearts", 3, "hearts"],
    ["four of hearts", 4, "hearts"],
    ["five of hearts", 5, "hearts"],
    ["six of hearts", 6, "hearts"],
    ["seven of hearts", 7, "hearts"],
    ["eight of hearts", 8, "hearts"],
    ["nine of hearts", 9, "hearts"],
    ["ten of hearts", 10, "hearts"],
    ["jack of hearts", 11, "hearts"],
    ["queen of hearts", 12, "hearts"],
    ["king of hearts", 13, "hearts"],

    ["ace_of_spades", 14, "spades"],
    ["two_of_spades", 2, "spades"],
    ["three_of_spades", 3, "spades"],
    ["four_of_spades", 4, "spades"],
    ["five_of_spades", 5, "spades"],
    ["six_of_spades", 6, "spades"],
    ["seven_of_spades", 7, "spades"],
    ["eight_of_spades", 8, "spades"],
    ["nine_of_spades", 9, "spades"],
    ["ten_of_spades", 10, "spades"],
    ["jack_of_spades", 11, "spades"],
    ["queen_of_spades", 12, "spades"],
    ["king_of_spades", 13, "spades"],
    
    #diamonds
    ["ace_of_diamonds", 14, "diamonds"],
    ["two_of_diamonds", 2, "diamonds"],
    ["three_of_diamonds", 3, "diamonds"],
    ["four_of_diamonds", 4, "diamonds"],
    ["five_of_diamonds", 5, "diamonds"],
    ["six_of_diamonds", 6, "diamonds"],
    ["seven_of_diamonds", 7, "diamonds"],
    ["eight_of_diamonds", 8, "diamonds"],
    ["nine_of_diamonds", 9, "diamonds"],
    ["ten_of_diamonds", 10, "diamonds"],
    ["jack_of_diamonds", 11, "diamonds"],
    ["queen_of_diamonds", 12, "diamonds"],
    ["king_of_diamonds", 13, "diamonds"],
    
    #clubs
    ["ace_of_clubs", 14, "clubs"],
    ["two_of_clubs", 2, "clubs"],
    ["three_of_clubs", 3, "clubs"],
    ["four_of_clubs", 4, "clubs"],
    ["five_of_clubs", 5, "clubs"],
    ["six_of_clubs", 6, "clubs"],
    ["seven_of_clubs", 7, "clubs"],
    ["eight_of_clubs", 8, "clubs"],
    ["nine_of_clubs", 9, "clubs"],
    ["ten_of_clubs", 10, "clubs"],
    ["jack_of_clubs", 11, "clubs"],
    ["queen_of_clubs", 12, "clubs"],
    ["king_of_clubs", 13, "clubs"]]
    
    return cards
cards = construct()
def name(card):
    return card[0]
def number(card):
    return card[1]
def suit(card):
    return card[2]
def indices(card1, card2):
    uno = 14 - number(card1)
    dos = 14 - number(card2)
    uno1 = min(uno, dos)
    dos2 = max(uno, dos)
    if (suit(card1) == suit(card2)):
        return uno1, dos2
    else:
        return dos2, uno1

def sort(hand):
    numbers = [number(card) for card in hand]
    new_numbers = []
    while numbers:
        new_numbers += [min(numbers)]
        numbers.remove(min(numbers))
    return new_numbers
