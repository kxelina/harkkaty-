class Trie:
    def __init__(self):
        self.nodes = [None] *26
        self.is_terminal = False

    def insert(self, word):

        if word not in self.nodes:
            self.nodes[i] 

    def search(self, word):
        word = word.lower()
        #print(f"hello{word}")
        # for n in range(0, len(word)):
        letter = word[0]
        # print(self.nodes[i]) 
        print(f"{letter}, {self.is_terminal}")
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
        
        
    def save_dictonary_to_trie(self, file):
        with open(file, "r") as file:
            for word in file:
                #word = i.strip()
                self.insert(word)

    def tets_save(self):
        x = Trie()
        self.nodes[0] = x
        y= Trie()
        x.nodes[2] = y
        x.is_terminal = True
        
        

        
