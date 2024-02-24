import re


class Node:
    '''Trien node luokka.'''

    def __init__(self):
        '''Alustaa noden.'''
        self.children = [None] * 26
        self.is_terminal = False
        self.value = ""


class Trie:
    '''Trie puurakenteen luokka.'''

    def __init__(self):
        '''Alustaa Trien luomalla noden.'''
        self.node = Node()

    def cleaner(self, word):
        ''' Muuttaa tekstin pienemmiksi kirjammiksi ja poistaa kaikki muut paitsi kirjaimet a-z.'''
        word = word.lower()
        word = re.sub("[^a-z]", "", word, re.M)
        return word

    def insert(self, key):
        '''Lisää sanan trien puurakenteeseen.'''
        curr_node = self.node
        key = self.cleaner(key)
        for i in range(0, len(key)):
            letter = key[i]
            letter_num = ord(letter)-ord("a")
            if curr_node.children[letter_num] is None:
                curr_node.children[letter_num] = Node()
                curr_node.children[letter_num].value = letter
            curr_node = curr_node.children[letter_num]
        curr_node.is_terminal = True

    def search(self, key):
        '''Etsii sanan trien puurakenteesta ja palauttaa löytykö se.'''
        curr_node = self.node
        key = self.cleaner(key)
        for i in range(0, len(key)):
            letter = key[i]
            letter_num = ord(letter)-ord("a")
            if curr_node.children[letter_num] is None:
                return False
            curr_node = curr_node.children[letter_num]
        return curr_node.is_terminal

    def save_dictonary_to_trie(self, dictonary_path):
        '''Käy läpi sanakirjan sanoja ja lisää sanat trie puurakenteeseen.'''
        with open(dictonary_path, "r", encoding='UTF-8') as file:
            for word in file:
                self.insert(word)
