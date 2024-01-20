from entities.word_dictionary import Trie

def main():
#    print("hello")
    trie = Trie()
#    trie.save_dictonary_to_trie("../data/ap_wordlist.txt")
#    trie.search("apart")
    trie.tets_save()
    print(trie.search("a"))
    # print(trie.search("A"))
    # print(trie.search("z"))
    # print(trie.search("ac"))
    print(trie.search("ac"))



if __name__ == "__main__":
    main()