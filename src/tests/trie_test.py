import unittest
from entities.trie import Trie


class Testtrie(unittest.TestCase):
    def test_insert_words_into_trie(self):
        trie = Trie()
        trie.insert("apartment")
        word = trie.search("apartment")
        self.assertEqual(word, True)  # sana löytyi

        trie.insert("apple")
        word = trie.search("apple")
        self.assertEqual(word, True)  # eri sana löytyi

        trie.insert("")
        word = trie.search("apartmen")
        self.assertEqual(word, False)  # väärin kirjoitettu sana ei löytynyt

        trie.insert("BIG")  # pystyy lisää isoilla kirjaimilla olevan sanan
        word = trie.search("big")
        self.assertEqual(word, True)  # sana on löytyy

        word = trie.search("apartmente")
        self.assertEqual(word, False)  # väärin kirjoitettu sana ei löytynyt

        # isoilla kirjaimilla kirjoitettu sana on löytynyt
        word = trie.search("APARTment")
        self.assertEqual(word, True)

        word = trie.search("!")
        self.assertEqual(word, True)  # ei ole kirjoitusvirhettä merkillä

    def test_save_dictonary_file_to_trie(self):
        trie = Trie()
        trie.save_dictonary_to_trie("src/data/test_wordslist.txt")
        found = trie.search("apartment")  # löytyi sanakirjasta
        self.assertEqual(found, True)

        # löytyy sanakirjasta, vaikka on kirjoitettu osan isolla kirjailla
        found = trie.search("APart")
        self.assertEqual(found, True)

        found = trie.search("ap")  # ei löytynyt sanaa
        self.assertEqual(found, False)
