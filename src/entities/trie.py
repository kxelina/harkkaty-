import re
from entities.distance import Distance


class Trie:
    def __init__(self):
        self.nodes = [None] * 26
        self.is_terminal = False
        self.value = ""

    # def __str__(self):
    #     return f"value:{self.value}, terminal:{self.is_terminal}, nodes: {self.nodes}"

    def cleaner(self, word):
        word = word.lower()
        word = re.sub("[^a-z]", "", word, re.M)
        # print(f" alku'{word}'")
        return word

    def insert(self, word, label=""):
        # print(f" helo'{word}'")
        # print(ord(word[0])-ord("a"))
        word = self.cleaner(word)
        if word == "" or word is None:
            return
        # print(f" loppu'{word}'")

        letter = word[0]
        letter_num = ord(letter)-ord("a")
        next_node = self.nodes[letter_num]

        if next_node is None:
            next_node = self.nodes[letter_num] = Trie()
            next_node.value = label+letter

        rest_letters = word[1:]
        # print(f"rest[{rest_letters}]")
        if rest_letters == "":
            # next_node.value = label+letter
            next_node.is_terminal = True
            # print("loppu")
            return self.is_terminal
        return next_node.insert(rest_letters, label+letter)

    def search(self, word):
        word = self.cleaner(word)
        if word == "" or word is None:
            return
        letter = word[0]
        # print(f"{letter}, {self.is_terminal}")
        # print(self.nodes)
        letter_num = ord(letter)-ord("a")
        # print(letter_num)
        # print(self.nodes[letter_num])
        next_node = self.nodes[letter_num]
        if next_node is None:
            # print(f"letternum{letter_num}")
            return False

        rest_letters = word[1:]
        # print(f"moi{rest_letters}")
        if rest_letters == "":
            # print(f"loppu{self.is_terminal}{self.nodes[letter_num]}")
            return next_node.is_terminal
        return next_node.search(rest_letters)
        # return self.is_terminal

    def save_dictonary_to_trie(self, filepath):
        with open(filepath, "r") as file:
            for word in file:
                # print(word)
                self.insert(word)

    def get_suggestions(self, word, min_distance=100, found_word=None):
        # print(f"aloitus-{word}-{min_distance}")

        if self.search(word):
            return word

        distance = Distance()

        for i in self.nodes:
            if i is None:
                continue

            if i.is_terminal:
                # print(f"sana löyty-----{i.value}")
                # first_word = i.value
                result = distance.distance(
                    i.value, word)
                # min_distance = result
                # print(f"sanan distance{result}")
                # print(min_distance)
                if result < min_distance:
                    # print("löyty parempi//////")
                    min_distance = result
                    found_word = [i.value]
                    # print(min_distance)

                elif result == min_distance:
                    found_word.append(i.value)
                    # print(f"löyty sama.....{i.value}")

            # print(f"käy läpi uusik:{word}--{min_distance}--{i.value}")
            (found_word, min_distance) = i.get_suggestions(
                word, min_distance, found_word)
        return (found_word, min_distance)

    # def print_words(self):
    #     # letter = word[0]
    #     for i in self.nodes:
    #         if i == None:
    #             continue

    #         if i.is_terminal == True:
    #             print(i.value)
    #         i.print_words()
        # print(f"{letter}, {self.is_terminal}")
        # print(self.nodes)
        # letter_num = ord(letter)-ord("a")
        # print(letter_num)
        # print(self.nodes[letter_num])
        # if self.nodes[letter_num] is None:
        #     return False

        # rest_letters = word[1:]
        # #print(f"moi{rest_letters}")
        # if rest_letters == "":
        #     return self.is_terminal
        # return self.nodes[letter_num].search(rest_letters)
