from stats import get_word_count 
from stats import count_characters
from stats import get_sorted_dict

def get_book_text (filepath):
    with open(filepath) as book:
        file_contents = book.read()
        return file_contents
    
     

def main():
    filepath = "books/frankenstein.txt"
    contents = get_book_text(filepath)
    word_count = get_word_count(contents)
    count_dict = count_characters(contents)
    sorted_list = get_sorted_dict(count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        char = i["char"]
        count = i["count"]
        print(f"{char}: {count}")
    print("============= END ===============")


main()
