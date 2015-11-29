from __future__ import print_function
import random 
def print_board():
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
             4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4] ### This is the exact board(Found online)

    for number in board:
        if number == 5:
            print('\n\n'),
        elif number == 4:
            print(' TW', end=' ')
        #print 'TW',
        elif number == 3:
            print(' DW', end=' ')
        #print 'DW',
        elif number == 2:
            print(' TL', end=' ')
        #print 'TL',
        elif number == 1:
            print(' DL', end=' ')
        #print 'DL',
        elif number == 0:
            print('___', end='  '),
 def begin_scrabble_draw():
    import random
    x =({"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 5, "i": 1, "h": 4, "k": 5, "j": 8, "m": 2, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 4, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 5, "v": 4, "y": 5, 
         "x": 10, "z": 10})
    return random.choice(x)
  
def scrabble_score(word):
    total = []
    for letter in word:
        total.append(score[letter.lower()])
    return sum(total)

def count_letters(word):
  count = {} 
  for letter in word:
    if letter not in count: count[letter] = 0
    count[letter] += 1 
  return count 



def spellable_word(word, rack):
    valid_words = []
    words = word_reader('/usr/share/dict/words')
    scored =  ((score_word(word), word) for word in words if set(word).issubset(set(rack)) and len(word) > 1 and spellable(word, rack))
    word_count = count_letters(word)
    rack_count  = count_letters(rack)
    return all([word_count[letter] <= rack_count[letter] for letter in word])
