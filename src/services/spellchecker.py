import re
from entities.trie import Trie
from entities.distance import Distance


class SpellChecker:
    def __init__(self):
        self.trie = Trie()
        self.trie.save_dictonary_to_trie("src/data/test_wordslist.txt")
        self.distance_calculator = Distance()

    def clean_paragraph(self, paragraph):
        pass

    def check_text(self, text):
        words = re.findall(r'\w+|[^\w]+', text)
        print(words)
        result = ""
        for i in words:
            print(i)
            result += i+""
        return result

    def print_words(self, prev_key=""):
        for letter in self.children:
            if letter is None:
                continue
            new_key = prev_key + letter.value
            if letter.is_terminal:
                print(f"{new_key}: {letter}")

            # else:
            #     print(f"{prev_letters}-{i}") #i.value
            letter.print_words(new_key)

    def get_correct_word(self, word):
        if self.trie.search(word):
            return word
        return self._get_suggestion(self.trie.node, word)

    def _get_suggestion(self, node, word, min_distance=100,  prev_key=None, found_word=None):
        # print(f"tässä{node},  {word}")
        for letter in node.children:
            if letter is None:
                continue
            if prev_key is None:
                new_key = letter.value
            else:
                new_key = prev_key + letter.value
            if letter.is_terminal:
                print(f"hello-{new_key}")
                distance = Distance()
                # print(f"sana löyty-----{i.value}")
                # first_word = i.value
                result = distance.distance(
                    new_key, word)
                # print(result)
                # min_distance = result
                # print(f"sanan distance{result}")
                # print(min_distance)
                if result < min_distance:
                    # print("löyty parempi//////")
                    min_distance = result
                    found_word = [new_key]
                    # print(min_distance)

                elif result == min_distance:
                    if found_word is not None:
                        found_word.append(new_key)
                    # print(f"löyty sama.....{i.value}")

            # print(f"käy läpi uusik:{word}--{min_distance}--{letter}")
            (found_word, min_distance) = self._get_suggestion(letter,
                                                              word, min_distance, new_key, found_word)
        return (found_word, min_distance)
