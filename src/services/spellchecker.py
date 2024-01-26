

from entities.trie import Trie
from entities.distance import Distance


class SpellChecker:
    def __init__(self):
        self.trie = Trie()
        self.trie.save_dictonary_to_trie("src/data/ap_wordslist.txt")
        self.distance_calculator = Distance()

    def clean_paragraph(self, paragraph):
        pass
