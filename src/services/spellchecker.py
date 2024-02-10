import re
from entities.trie import Trie
from entities.distance import Distance


class SpellChecker:
    '''Sanan oikeinkirjoituksen tarkistuksen luokka.'''

    def __init__(self, dictonary_path):
        '''Alustaa trie tietorakenteen ja etäisyys algoritmin.'''
        self.trie = Trie()
        self.trie.save_dictonary_to_trie(dictonary_path)
        self.distance_calculator = Distance()

    def check_text(self, text):
        '''Palauttaa listan tekstin elementeistä (sanoja tai merkkejä) korjaksineen 
        ja korjatus elementit palautuu tuplena.'''
        words = re.findall(r'\w+|[^\w]+', text)
        suggestions = []
        for word in words:
            if len(word) > 1 and ord("z") >= ord(word[0]) >= ord("a"):
                suggestions.append(self.get_correct_word(word))
            else:
                suggestions.append(word)
        return suggestions

    def fix_text(self, user_input):
        '''Palauttaa tekstin korjattuna käyttäen ensimmäistä ehdotusta.'''
        clean_paragraph = self.check_text(user_input)
        result = ""
        for element in clean_paragraph:
            if isinstance(element, tuple):
                result += element[0][0]
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

    def get_correct_word(self, word):
        '''Palauttaa oikeaan kirjoitetun sanan tai ehdotuksen.'''
        if self.trie.search(word):
            return word
        return self._get_suggestion(self.trie.node, word)

    def _get_suggestion(self, node, word, min_distance=100,  prev_key=None, found_word=None):
        '''Palauttaa väärinkirjoitetulle sanalle ehdotuksen ja käy läpi trie puurakennetta 
        ja käyttää etäisyys algoritmiä.'''
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

    #         #print(f"nyut-{word[i]}-{alku}")
    #         #print(alku+word[i])
    #         print(f"{alku+word [i]}-{self.get_correct_word(alku+word[i])}")
    #         alku +=  word[i]
    #         #print(alku+word[i+1])

    #     return True
