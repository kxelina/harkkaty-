import unittest
from services.spellchecker import SpellChecker


class TestSpellchecker(unittest.TestCase):
    def test_get_correct_word(self):
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

    def test_optimal_get_correct_word(self):
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

    # def test_get_fixed_text(self):
    #     spellchecker = SpellChecker(
    #         "src/data/test_wordslist.txt", "src/data/3000_words.txt")
    #     text = spellchecker.fix_text("apartment...2 apar jjj!banana dont\n!")
    #     # testailee eri merkkejä ja erilaisia sanoja
    #     red_start = "\033[91m"
    #     red_end = "\033[0m"
    #     self.assertEqual(
    #         text, f"apartment...2 {red_start}apart{red_end} {red_start}jet{red_end}!{red_start}balance{red_end} {red_start}adopt{red_end}\n!")  # sanakirjassa ei ole banana ja dont sanaa
    #     # testailee järkevän tekstin
    #     text = spellchecker.fix_text(
    #         "hello, what, where are you?")
    #     self.assertEqual(
    #         text, f"hello, what, where {red_start}area{red_end} you?")  # sanakirjassa ei ole are sanaa
