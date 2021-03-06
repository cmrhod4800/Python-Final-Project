from __future__ import print_function

import random ### I had to import random for the scrabble_draw function

def print_board():### How can I print the players word on the board ???
    for number in board:
        if number == 5:
            print('\n\n'),
        elif number == 4:
            print(' TW', end=' ')
        #print 'Tripple word score',
        elif number == 3:
            print(' DW', end=' ')
        #print 'Double word score',
        elif number == 2:
            print(' TL', end=' ')
        #print 'Tripple letter score',
        elif number == 1:
            print(' DL', end=' ')
        #print 'Double letter score',
        elif number == 0:
            print('___', end='  '),

def scrabble_draw(draws=7): ### This will generate seven letters for the player.
                            ### This will work until the dictionary runs out of standard letters. 
    """ A player is given seven letter tiles blindly.This function will exicute that. To do this
is best exicuted by using and calling upon the random tool built into python.However, when the given
letter tiles are used up just like the real game, this function will print "Not enough letters to draw".

>>> scrabble_draw()
['j', 'k', 'b', 'j', 'm', 'v', 'h']
>>> scrabble_draw()
['u', 't', 'n', 'i', 's', 'r', 'd']
>>> scrabble_draw()
['k', 'c', 'y', 'v', 'b', 'p', 'd']
>>> scrabble_draw()


    """
    letters = []
    while len(letters) < draws:
        letter = random.choice(letter_pool.keys())
        if letter_pool[letter] > 0:
            letters.append(letter)
            letter_pool[letter] -= 1
        if sum(letter_pool.values()) == 0:
            print("Not enough letters to draw!")
            return letters
    return letters
def Pleyers_word():
    if players word in rack:
        print word on board

    
def scrabble_score(word): ### This will calculate the players score
    """ This is where the players score is calculated from the standard scabble scores.
Rangining from 1 to 10 based on letter occurance in the English Language.
>>> "World"
>>> 10
>>> "Python"
>>> 16
>>> "North"
>>> 8


"""
    total = 0
    for i in word:
        total = total+score[i.lower()]
    return total

def count_letters(word):
  count = {} 
  for letter in word:
    if letter not in count: count[letter] = 0
    count[letter] += 1 
  return count 

def spellable_word(word, rack): ### starting point for placeing players word on board
    valid_words = []

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 5, "i": 1, "h": 4, "k": 5, "j": 8, "m": 2, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 4, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 5, "v": 4, "y": 5, 
         "x": 8, "z": 10}

letter_pool = {"a": 8, "c": 1, "b": 2, "e": 8, "d": 5, "g": 3, 
               "f": 2, "i": 5, "h": 2, "k": 3, "j": 1, "m": 3, 
               "l": 5, "o": 5, "n": 5, "q": 3, "p": 2, "s": 8, 
               "r": 4, "u": 3, "t": 8, "w": 2, "v": 2, "y": 2, 
               "x": 2, "z": 13}

board = [4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4, 5,
         0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0, 5,
         0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0, 5,
         1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1, 5,
         0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 5,
         0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 5,
         0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 5,
         4, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 4, 5,
         0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 5,
         0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 5,
         0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 5,
         1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1, 5,
         0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0, 5,
         0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0, 5,
         4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4]


if __name__ == "__main__":
    print(scrabble_score("North"))### This is where the player will put their
                                ### Desired word     
    run_game = True
    print("Welcome to the game! Would you like to play Scrabble?")
    while run_game is True:
        print("""\n(P) to print the board\n

Press (Q) to quit.""")
        choice = raw_input("Enter a selection: ")

        if choice in ['Q', 'q']:
            run_game = False
        elif choice in ['P', 'p']:
            print_board()
        
        
  

        

