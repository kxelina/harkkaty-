import time
from services.spellchecker import SpellChecker


def main():
    start_time = time.time()

    spell_checker = SpellChecker()
    print(spell_checker.get_correct_word("apend"))
    # user_input = input("Enter a text paragraph: ")
    # suggestions = trie.get_suggestions(user_input)
    # print(suggestions)
    # corrected_text = spell_checker

    # print(f"\nCorrected Text:\n{corrected_text}")
    # print(f"{(time.time() - start_time)}")
    # result = spell_checker.check_text("hello how are you!")
    # print(result)


if __name__ == "__main__":
    main()
