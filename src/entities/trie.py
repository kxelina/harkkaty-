import re
# from entities.distance import Distance


class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_terminal = False
        self.value = ""

    # def __str__(self):
    #     return f"value:{self.value}, terminal:{self.is_terminal}, nodes: {self.children}"

    # def print_words(self, prev_key=""):
    #     for letter in self.children:
    #         if letter is None:
    #             continue
    #         new_key = prev_key + letter.value
    #         if letter.is_terminal:
    #             print(f"{new_key}: {letter}")

    #         # else:
    #         #     print(f"{prev_letters}-{i}") #i.value
    #         letter.print_words(new_key)


class Trie:
    def __init__(self):
        self.node = Node()

    # def __str__(self):
    #     return f"value:{self.node.value}, terminal:{self.node.is_terminal}, nodes: {self.node.children}"

    def cleaner(self, word):
        word = word.lower()
        word = re.sub("[^a-z]", "", word, re.M)
        return word

    def insert(self, key):
        # ord(key[i])
        curr_node = self.node
        key = self.cleaner(key)
        for i in range(0, len(key)):
            letter = key[i]
            letter_num = ord(letter)-ord("a")
            if curr_node.children[letter_num] == None:
                curr_node.children[letter_num] = Node()
                curr_node.children[letter_num].value = letter
            curr_node = curr_node.children[letter_num]
        curr_node.is_terminal = True

    def search(self, key):
        curr_node = self.node
        key = self.cleaner(key)
        for i in range(0, len(key)):
            letter = key[i]
            letter_num = ord(letter)-ord("a")
            if curr_node.children[letter_num] == None:
                return False
            curr_node = curr_node.children[letter_num]
        return curr_node.is_terminal

    def save_dictonary_to_trie(self, filepath):
        with open(filepath, "r") as file:
            for word in file:
                self.insert(word)
