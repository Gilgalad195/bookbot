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