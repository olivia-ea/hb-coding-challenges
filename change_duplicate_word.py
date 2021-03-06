import unittest
from random import shuffle

def reverse_word(word):
    split_word = list(word)
    split_word.reverse()

    return ''.join(split_word)

def change_duplicate_word(phrase):
    
    track_words = []

    for word in phrase.split():
        if word not in track_words:
            track_words.append(word)
        else:
            new_word = split_word(word)
            track_words.append(new_word)
    return ' '.join(track_words)
