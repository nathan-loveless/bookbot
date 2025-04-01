import sys
from stats import get_num_words
from stats import get_num_chars
from stats import generate_report

def get_book_text(file_path):
    num_words = 0
    text = ""
    with open(file_path) as f:
        
        text = f.read()

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_dict = get_num_chars(text)
    print(char_dict)
    generate_report(char_dict, num_words)
    


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_book_text(sys.argv[1])


main()