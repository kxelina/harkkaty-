import re
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
                correct_words = self.get_correct_word(clean_word, word)
                suggestions.append(correct_words)
            else:
                suggestions.append(word)
        return suggestions

    # def fix_text(self, user_input):
    #     '''Palauttaa tekstin korjattuna käyttäen ensimmäistä ehdotusta.'''
    #     clean_paragraph = self.check_text(user_input)
    #     result = ""
    #     for element in clean_paragraph:
    #         if isinstance(element, tuple):
    #             result += f"\033[91m{element[0]}\033[0m"
    #         else:
    #             result += element
    #     return result

    def get_correct_word(self, word, orginal_word=None):
        '''Palauttaa oikeaan kirjoitetun sanan tai ehdotuksen.'''
        if self.trie_full.search(word):
            return word
        if orginal_word is None:
            orginal_word = word
        found_words = []
        # Lisää 1.kirjaimen ja katsoo löytyykö sanakirjasta oikeaa sanaa
        for i in range(ord("a"), ord("z")):
            proposed_word = chr(i)+word
            if self.trie_full.search(proposed_word):
                found_words.append(proposed_word)
        # Lisää viimeisen kirjaimen
            proposed_word = word+chr(i)
            if self.trie_full.search(proposed_word):
                found_words.append(proposed_word)
        # Ottaa pois 1.kirjaimen
        if self.trie_full.search(word[1:]):
            found_words.append(word[1:])
        # Ottaa pois viimeisen kirjaimen
        if self.trie_full.search(word[:-1]):
            found_words.append(word[:-1])

        if found_words:
            return (found_words, 0.5, orginal_word)

        result = self._get_suggestion(
            self.trie.node, word, orginal_word=orginal_word)
        # Jos distance ei ole 1 eli hyvä, niin jatketaan etsimistä isosta sanakirjasta
        if result[1] != 1:
            result = self._get_suggestion(
                self.trie_full.node, word, orginal_word=orginal_word)
        return result

    def _get_suggestion(
            self, node, word, min_distance=100, prev_key=None, found_word=None, orginal_word=None):
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
            (found_word, min_distance, orginal_word) = self._get_suggestion(
                letter, word, min_distance, new_key, found_word, orginal_word)
        return (found_word, min_distance, orginal_word)
