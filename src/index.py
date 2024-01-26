from entities.trie import Trie
#from entities.distance import Distance
from services.spellchecker import SpellChecker

def main():
    trie = Trie()
    #distance = Distance()
    trie.save_dictonary_to_trie("src/data/ap_wordslist.txt")
    # trie.print_words()
    #print(trie)
    # print(f"hello{trie.nodes}")
    # print(trie.nodes[1])
    # print(trie.nodes[0].nodes[15].nodes[15])
    # print(trie.nodes[0].nodes[15].nodes[15].nodes[17])
    # print(trie.nodes[0].nodes[15].nodes[15].nodes[17].nodes[14])
    # print(trie.nodes[0].nodes[15].nodes[15].nodes[17].nodes[14].nodes[23])
    # print(trie.nodes[0].nodes[15].nodes[15].nodes[17].nodes[14].nodes[23].nodes[8])
#    trie.search("apart")
    #trie.test_save2()
    #print(trie.search("APART"))
    # print(trie.search("A"))
    # print(trie.search("z"))
    # print(trie.search("aa"))
    # print(trie.search("apa"))
    # print(trie.search("apparentl"))
    print(trie.get_suggestions("appro", 100, ""))
    # print(distance.optimal_string_alignment_distance("apart", "bpart"))
    # print(distance.optimal_string_alignment_distance("ab", "abba"))
    #spell_checker = SpellChecker()

    # user_input = input("Enter a text paragraph: ")
    # corrected_text = spell_checker

    # print(f"\nCorrected Text:\n{corrected_text}")


if __name__ == "__main__":
    main()