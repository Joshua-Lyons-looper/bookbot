def get_num_words(content):
    num_words = len(content.split())
    print(f"{num_words} words found in the document")
    return num_words

def count_characters(content):
    letter_count = {}
    for letter in content:
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count



def sort_and_format(letter_dict):
    return_list = []
    for char, count in letter_dict.items():
        return_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
    
    return_list.sort(reverse=True,key=sort_on)

    return return_list


