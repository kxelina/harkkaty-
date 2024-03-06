import unittest
from services.spellchecker import SpellChecker


class TestSpellchecker(unittest.TestCase):
    def test_get_correct_word_function(self):
        spellchecker = SpellChecker(
            "src/data/test_wordslist.txt", "src/data/3000_words.txt")
        # sana on väärin, joten antaa läheisempiä ehdotuksia
        word = spellchecker.get_correct_word("apend")
        self.assertEqual(word[0], [
            'abend', 'agend', 'amend', 'anend', 'aped', 'append', 'arend', 'pend', 'spend', 'upend'])
        # agend sana ei ole 3000-word listassa
        word = spellchecker.get_correct_word("agend", "Agend")
        self.assertEqual(word, (['agenda'], 0.5, 'Agend'))
        correct_word = spellchecker.get_correct_word(
            "bake")  # sana löytyi 3000-word listasta
        self.assertEqual(correct_word, "bake")

    def test_optimal_get_correct_word_function(self):
        spellchecker = SpellChecker(
            "src/data/test_wordslist.txt", "src/data/3000_words.txt")
        word = spellchecker.get_correct_word(
            "partment")  # sanasta puutuu alkukirjain
        self.assertEqual(word, (['apartment'], 0.5, 'partment'))
        word = spellchecker.get_correct_word(
            "apartmen")  # sanasta puutuu loppukirjain
        self.assertEqual(word, (['apartment'], 0.5, 'apartmen'))
        # sanassa on ylimääräinen alkukirjain
        word = spellchecker.get_correct_word("aapartment")
        self.assertEqual(word, (['apartment'], 0.5, 'aapartment'))
        # sanassa on ylimääräinen loppukirjain
        word = spellchecker.get_correct_word("apartmentt")
        self.assertEqual(word, (['apartment'], 0.5, 'apartmentt'))
        # sanaa ei löytynyt pienesta sanakirjasta ja siiryttiin etsimään isosta sanakirjasta
        word = spellchecker.get_correct_word("runny")
        self.assertEqual(word, (['funny'], 1, 'runny'))

    def test_check_text_function(self):
        spellchecker = SpellChecker(
            "src/data/test_wordslist.txt", "src/data/3000_words.txt")
        text = spellchecker.check_text(" Hello i am a athele!\n!")
        # testailee eri merkkejä ja erilaisia sanoja sekä väärän sanan
        self.assertEqual(
            text, [' ', 'hello', ' ', 'i', ' ', 'am', ' ', 'a', ' ',
                   (['athlete', 'theme', 'there', 'these'], 2, 'athele'), '!\n!'])
        text = spellchecker.check_text("what is my name?")
        # testailee oikean kirjoitetun tekstin
        self.assertEqual(
            text, ['what', ' ', 'is', ' ', 'my', ' ', 'name', '?'])
