from entities.trie import Trie

def main():
#    print("hello")
    trie = Trie()
    trie.save_dictonary_to_trie("src/data/ap_wordslist.txt")
    # print(trie)
    # print(trie.nodes[0])
    # print(trie.nodes[0].nodes[15])
    # print(trie.nodes[0].nodes[15].nodes[15])
    # print(trie.nodes[0].nodes[15].nodes[15].nodes[17])
    # print(trie.nodes[0].nodes[15].nodes[15].nodes[17].nodes[14])
    # print(trie.nodes[0].nodes[15].nodes[15].nodes[17].nodes[14].nodes[23])
    # print(trie.nodes[0].nodes[15].nodes[15].nodes[17].nodes[14].nodes[23].nodes[8])
#    trie.search("apart")
    #trie.test_save2()
    #print(trie.search("a"))
    # print(trie.search("A"))
    # print(trie.search("z"))
    # print(trie.search("aa"))
    print(trie.search("apa"))
    print(trie.search("apparentl"))



if __name__ == "__main__":
    main()