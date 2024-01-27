import unittest
from entities.trie import Trie


class Testtrie(unittest.TestCase):
    def test_insert_words_into_trie(self):
        trie = Trie()
        trie.insert("apartment")
        word = trie.search("apartment")
        self.assertEqual(word, True)

        trie.insert("apple")
        word = trie.search("apple")
        self.assertEqual(word, True)

        trie.insert("")
        word = trie.search("apartmen")
        self.assertEqual(word, False)

        word = trie.search("apartmente")
        self.assertEqual(word, False)

        word = trie.search("APARTment")
        self.assertEqual(word, True)

        word = trie.search("")
        self.assertEqual(word, None)

    def test_save_dictonary_to_trie(self):
        trie = Trie()
        trie.save_dictonary_to_trie("src/data/test_wordslist.txt")
        found = trie.search("apartment")
        self.assertEqual(found, True)

        found = trie.search("APart")
        self.assertEqual(found, True)

        found = trie.search("ap")
        self.assertEqual(found, False)

    def test_get_suggestions(self):
        trie = Trie()
        trie.save_dictonary_to_trie("src/data/test_wordslist.txt")
        suggestions = trie.get_suggestions("apend")
        self.assertEqual(suggestions[0], [
                         'abend', 'agend', 'amend', 'anend', 'aped', 'append', 'arend', 'pend', 'spend', 'upend'])
        suggestions = trie.get_suggestions("agend")
        self.assertEqual(suggestions, "agend")
