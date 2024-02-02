import unittest
from services.spellchecker import SpellChecker


class TestSpellchecker(unittest.TestCase):
    def test_get_correct_word(self):
        spellchecker = SpellChecker("src/data/test_wordslist.txt")
        correct_word = spellchecker.get_correct_word("apend")
        self.assertEqual(correct_word[0], [
                         'abend', 'agend', 'amend', 'anend', 'aped', 'append', 'arend', 'pend', 'spend', 'upend'])
        correct_word = spellchecker.get_correct_word("agend")
        self.assertEqual(correct_word, "agend")

    def test_get_fixed_text(self):
        spellchecker = SpellChecker("src/data/test_wordslist.txt")
        text = spellchecker.fix_text("apartment...2 apar jjj!banana dont\n!")
        self.assertEqual(text, "apartment...2 apart aped!anend pend\n!")
