import time
from services.spellchecker import SpellChecker


def main():
    #alku = time.time()
    spell_checker = SpellChecker(
        "src/data/3000_words.txt", "src/data/words_alpha.txt")
    # loppu = time.time()
    # print(loppu-alku)
    # print(spell_checker.get_correct_word("apend"))
    user_input = input("Enter a text paragraph: ")#"apartment...2 apar jjj!banana dont bage\n!"
    # print("alku----")
#     user_input = '''Hello,
# My name is Susan. I'm forteen and I life in Germany. My hobbys are go to discos,
#    sometimes I hear music in the radio.
# In the summer I go bathing in a lake. I haven't any brothers or sisters. We take busses to scool.
# I visit year 9 at my school. My birthday is on Friday. I hope I will become a new guitar.
# I'm looking forward to get a e-mail from you.

# Yours,
#
    #user_input = "apartment...2 apar jjj!banana dont\n!"
    clean_text = spell_checker.fix_text(user_input)
    print(clean_text)
    # print(spell_checker.helper("hepetihop"))
    # 'abend', 'agend', 'amend', 'anend', 'aped', 'append', 'arend', 'pend', 'spend', 'upend'


if __name__ == "__main__":
    main()
