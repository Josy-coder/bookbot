def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total_words = read_words(file_contents)
        print("--- Report Begins ---")
        print(f"we have {total_words} in total")
        print("\n")
        print("\n")
        characters_and_count = characters_count(file_contents)
        for character, count in characters_and_count.items():
            print(f"This character {character} appear {count} times in the book")
        print("\n")
        print("\n")
        print("--- Reports Ends ---")

def read_words(file_contents):
    word_count = file_contents.split()
    return len(word_count)

def characters_count(file_contents):
    count = set(file_contents.lower())
    characters_dict = {}
    for character in count:
        if character.isalpha():
            characters_dict[character] = file_contents.count(character)
    return characters_dict



main()
