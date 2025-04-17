import sys
from stats import get_word_count 
from stats import count_characters
from stats import get_sorted_dict
from stats import print_report


def get_book_text (filepath):
    with open(filepath) as book:
        file_contents = book.read()
        return file_contents
    
     

def main(argv):
    if len(argv) == 2:
        filepath = argv[1]
        contents = get_book_text(filepath)
        word_count = get_word_count(contents)
        count_dict = count_characters(contents)
        sorted_list = get_sorted_dict(count_dict)
        print_report(filepath, word_count, sorted_list)
    else:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    


main(sys.argv)
