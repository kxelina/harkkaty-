from services.spellchecker import SpellChecker


def main():
    spell_checker = SpellChecker(
        "src/data/3000_words.txt", "src/data/words_alpha.txt")

    while True:
        # user_input = "apartment...2 apar runn!ahello dont\n!"
        user_input = input(
            "Enter a word or a text paragraph (type 'exit' to stop): ")

        if user_input.lower() == 'exit':
            break

        elements = spell_checker.check_text(user_input)
        corrected_text = ""

        for i, element in enumerate(elements):
            corrected_words = element[0]
            if isinstance(element, tuple):
                # print(element)
                print(f"Word {element[2]} suggestions:")
                for j, suggestion in enumerate(corrected_words, start=1):
                    print(f"{j}. {suggestion}")
                while True:
                    choice = input(
                        f"Choose replacement for word \033[91m{element[2]}\033[0m: ")
                    # print(f"chice: {choice, int(choice), len(element), choice.isdigit()}")
                    if not choice:
                        corrected_text += element[2]
                        break
                    if choice.isdigit() and 1 <= int(choice) <= len(corrected_words)+1:
                        corrected_text += corrected_words[int(choice)-1]
                        break
                    print("Invalid choice. Please enter a number corresponding to a suggestion.")
            else:
                corrected_text += element
        print(corrected_text)

        # fully_corrected_text = "".join(corrected_text)
        # print("Fully corrected text:")
        # print(fully_corrected_text)


if __name__ == "__main__":
    main()
