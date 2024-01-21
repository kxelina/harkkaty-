import re

class Trie:
    def __init__(self):
        self.nodes = [None] *26
        self.is_terminal = False
        self.value = ""

    def __str__(self):
        return f"value:{self.value}, terminal:{self.is_terminal}, nodes: {self.nodes}"
    
    def cleaner(self, word):
        word = word.lower()
        word = re.sub("[^a-z]", "", word, re.M)
        #print(f" alku'{word}'")
        return word

    def insert(self, word, label):
        # print(f" helo'{word}'")
        # print(ord(word[0])-ord("a"))
        word = self.cleaner(word)
        #print(f" loppu'{word}'")
        self.value = label
        letter = word[0]
        letter_num = ord(letter)-ord("a")
        
        if self.nodes[letter_num] is None:
            trie = Trie()
            self.nodes[letter_num] = trie
        
        rest_letters = word[1:]
        #print(f"rest[{rest_letters}]")
        if rest_letters == "":
            self.is_terminal = True
            #print("loppu")
            return self.is_terminal
        return self.nodes[letter_num].insert(rest_letters, label+letter)

    def search(self, word):
        letter = word[0]
        #print(f"{letter}, {self.is_terminal}")
        # print(self.nodes)
        letter_num = ord(letter)-ord("a")
        #print(letter_num)
        # print(self.nodes[letter_num])
        if self.nodes[letter_num] is None:
            return False
        
        rest_letters = word[1:]
        #print(f"moi{rest_letters}")
        if rest_letters == "":
            return self.is_terminal
        return self.nodes[letter_num].search(rest_letters)
        #return self.is_terminal
        
        
    def save_dictonary_to_trie(self, filepath):
        with open(filepath, "r") as file:
            for word in file:
                #print(f"word:{word}")
                #word = i.strip()
                self.insert(word, "")
                #print("tehty")

    # def tets_save(self):
    #     x = Trie()
    #     self.nodes[0] = x
    #     y= Trie()
    #     x.nodes[2] = y
    #     x.is_terminal = True

    # def test_save2(self):
    #     self.insert("ac")
        #self.insert("ac")
      
        
        

        
