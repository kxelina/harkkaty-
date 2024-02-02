import unittest
from services.spellchecker import SpellChecker


class TestSpellchecker(unittest.TestCase):
    def test_get_correct_word(self):
        spellchecker = SpellChecker()
        correct_word = spellchecker.get_correct_word("apend")
        self.assertEqual(correct_word[0], [
                         'abend', 'agend', 'amend', 'anend', 'aped', 'append', 'arend', 'pend', 'spend', 'upend'])
        correct_word = spellchecker.get_correct_word("agend")
        self.assertEqual(correct_word, "agend")
