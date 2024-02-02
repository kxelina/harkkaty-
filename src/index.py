from services.spellchecker import SpellChecker


def main():
    spell_checker = SpellChecker("src/data/words_alpha.txt")
    # print(spell_checker.get_correct_word("apend"))
    user_input = input("Enter a text paragraph: ")
    #user_input = "apartment...2 apar jjj!banana dont\n!"
    clean_text = spell_checker.fix_text(user_input)
    print(clean_text)


if __name__ == "__main__":
    main()
