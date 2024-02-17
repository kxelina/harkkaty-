import re
import time
from entities.trie import Trie
from entities.distance import Distance


class SpellChecker:
    '''Sanan oikeinkirjoituksen tarkistuksen luokka.'''

    def __init__(self, dictonary_path, dictonary_path_full):
        '''Alustaa trie tietorakenteen ja etäisyys algoritmin.'''
        self.trie = Trie()
        self.trie_full = Trie()

        self.trie.save_dictonary_to_trie(dictonary_path)
        self.trie_full.save_dictonary_to_trie(dictonary_path_full)
        self.distance_calculator = Distance()

    def check_text(self, text):
        '''Palauttaa listan tekstin elementeistä (sanoja tai merkkejä) korjaksineen 
        ja korjatus elementit palautuu tuplena.'''
        words = re.findall(r'\w+|[^\w]+', text)
        suggestions = []
        for word in words:
            clean_word = self.trie.cleaner(word)
            if len(clean_word) > 1 and ord("z") >= ord(clean_word[0]) >= ord("a"):
                correct_words = self.get_correct_word(clean_word)
                if correct_words is None:
                    suggestions.append((False, word))
                else:
                    suggestions.append(correct_words)
            else:
                suggestions.append(word)
        return suggestions

    def fix_text(self, user_input):
        '''Palauttaa tekstin korjattuna käyttäen ensimmäistä ehdotusta.'''
        clean_paragraph = self.check_text(user_input)
        result = ""
        for element in clean_paragraph:
            if isinstance(element, tuple):
                if element[0] is False:
                    result += f"{element[1]}(unknown word)"
                else:
                    result += f"--{element[0][0]}--"
            else:
                result += element
        return result
    # def print_words(self, prev_key=""):
    #     for letter in self.children:
    #         if letter is None:
    #             continue
    #         new_key = prev_key + letter.value
    #         if letter.is_terminal:
    #             print(f"{new_key}: {letter}")

    #         # else:
    #         #     print(f"{prev_letters}-{i}") #i.value
    #         letter.print_words(new_key)

    # def get_correct_word_orginal(self, word):
    #     '''Palauttaa oikeaan kirjoitetun sanan tai ehdotuksen.'''
    #     if self.trie.search(word):
    #         return word
    #     return self._get_suggestion(self.trie.node, word)

    def get_correct_word(self, word):
        '''Palauttaa oikeaan kirjoitetun sanan tai ehdotuksen.'''
        #alku = time.time()
        if self.trie_full.search(word):
            # loppu = time.time()
            # print(f"{loppu-alku}, löyty-{word}")
            return word
        # Lisää 1.kirjaimen ja katsoo löytyykö sanakirjasta oikeaa sanaa
        for i in range(ord("a"), ord("z")):
            if self.trie_full.search(chr(i)+word):
                # loppu = time.time()
                # print(f"{loppu-alku}, lisää alku-{word}")
                return ([chr(i)+word], 0.5)
        # Lisää viimeisen kirjaimen
        for i in range(ord("a"), ord("z")):
            if self.trie_full.search(word+chr(i)):
                # loppu = time.time()
                # print(f"{loppu-alku}, lisää loppu-{word}")
                return ([word+chr(i)], 0.5)
        # Ottaa pois 1.kirjaimen
        if self.trie_full.search(word[1:]):
            # loppu = time.time()
            # print(f"{loppu-alku}, eka kirjain-{word}")
            return ([word[1:]], 0.5)
        # Ottaa pois viimeisen kirjaimen
        if self.trie_full.search(word[:-1]):
            # loppu = time.time()
            # print(f"{loppu-alku}, vika kirjain-{word}")
            return ([word[:-1]], 0.5)
        # start = word[0]
        # end = word[1:]
        result = self._get_suggestion(self.trie.node, word)
        if result[1] == 1:
            # loppu = time.time()
            # print(f"{loppu-alku}, pieni-{word}")
            return result
        result = self._get_suggestion(self.trie_full.node, word)
        # loppu = time.time()
        # print(f"{loppu-alku}, loppu-{word}")
        return result

    def _get_suggestion(self, node, word, min_distance=100,  prev_key=None, found_word=None):
        '''Palauttaa väärinkirjoitetulle sanalle ehdotuksen ja käy läpi trie puurakennetta 
        ja käyttää etäisyys algoritmiä.'''
        # if node is None:
        #     return None
        for letter in node.children:
            if letter is None:
                continue

            if prev_key is None:
                new_key = letter.value

            else:
                new_key = prev_key + letter.value

            if letter.is_terminal:
                result = self.distance_calculator.distance(
                    new_key, word)

                if result < min_distance:
                    min_distance = result
                    found_word = [new_key]

                elif result == min_distance:
                    found_word.append(new_key)
            (found_word, min_distance) = self._get_suggestion(
                letter, word, min_distance, new_key, found_word)
        return (found_word, min_distance)

    # def helper(self, word):
    #     alku = ""
    #     for i in range(len(word)):
    #         print(f"{alku+word [i]}-{self.get_correct_word(alku+word[i])}")
    #         alku +=  word[i]

    #     return True
