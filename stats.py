def get_word_count(contents):
    words = contents.split()
    return len(words)


def count_characters(contents):
    char_list = list(contents.lower())
    c_dict = {}
    for c in char_list:
        if c in c_dict:
            c_dict[c] =  c_dict[c] + 1
        else:
            c_dict[c] = 1
    
    return c_dict

def get_sorted_dict(input_dict):
    chars_list = []
    def sort_on(dict):
        return dict["count"]
    for char, count in input_dict.items():
        if char.isalpha():
            chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list