from entities.trie import Trie
from entities.distance import Distance
from services.spellchecker import SpellChecker
import time


def main():
    trie = Trie()
    distance = Distance()
    # trie.save_dictonary_to_trie("src/data/ap_wordslist.txt")
    trie.save_dictonary_to_trie("src/data/test_wordslist.txt")
    start_time = time.time()
    # trie.print_words()
#    trie.search("apart")
    # trie.test_save2()
    # print(trie.search("APART"))
    # print(trie.search("A"))
    # print(trie.search("z"))
    # print(trie.search("aa"))
    # print(trie.search("apa"))
    # print(trie.search("apparentl"))
    # print(trie.get_suggestions("apend"))
    print("testataan 'appa' sanaa")
    print(trie.get_suggestions("appa"))
    # ['abend', 'agend', 'amend', 'anend', 'aped', 'append', 'arend', 'pend', 'spend', 'upend'], 1, 7,6s(oma:11,57s), 370000)
    # print(distance.distance("apend", "pe")) #3
    # print(distance.optimal_string_alignment_distance("apend", "pe"))
    # print(distance.optimal_string_alignment_distance("apend", "pend"))
    # print(distance.optimal_string_alignment_distance("apend", "p"))
    # spell_checker = SpellChecker()

    # user_input = input("Enter a text paragraph: ")
    # corrected_text = spell_checker

    # print(f"\nCorrected Text:\n{corrected_text}")
    print(f"{(time.time() - start_time)}")


if __name__ == "__main__":
    main()
