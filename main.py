from stats import get_word_count 
from stats import count_characters

def get_book_text (filepath):
    with open(filepath) as book:
        file_contents = book.read()
        return file_contents
    
     

def main():
    contents = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(contents)
    count_dict = count_characters(contents)
    print (f"{word_count} words found in the document")
    #print (count_dict)

    chars_list = []
    def sort_on(dict):
        return dict["count"]
    for char, count in count_dict.items():
        if char.isalpha():
            chars_list.append({"char": char, "count": count})
            chars_list.sort(reverse=True, key=sort_on)
    print(chars_list)

    #NOW I NEED TO GET THE DICTIONARY LIST BACK INTO A SINGLE KEY:VALUE PAIR DICTIONARY


main()
