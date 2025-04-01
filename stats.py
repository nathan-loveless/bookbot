def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    char_dict = {}
    for char in text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_descending(dict, key):
    pass

def generate_report(char_dict, word_count):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    sorted_dict = dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))
    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")
