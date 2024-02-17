from services.spellchecker import SpellChecker


def main():
    spell_checker = SpellChecker(
        "src/data/3000_words.txt", "src/data/words_alpha.txt")
    user_input = input("Enter a text paragraph: ")
    clean_text = spell_checker.fix_text(user_input)
    print(clean_text)


if __name__ == "__main__":
    main()
