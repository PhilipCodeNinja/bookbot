def main():
    filepath = "./books/frankenstein.txt"
    file_text = get_book_text(filepath)
    ## return dictionary with chars and count
    char_count_dict = char_counter(file_text)
    new_dict = char_dict_to_frequency_char_list(char_count_dict)

    ## return the word count
    word_count = word_counter(file_text)
    # print(word_count)

    ## print the text
    # print(file_text)

    # print report
    # print("--- Begin report of books/frankenstein.txt ---")
    # print(f"{word_count} words fount in the document.")
    # for key in char_count_dict.keys():
    #     printable_key = get_readable_char(key)
    #     print(f"The char '{printable_key}' was found {char_count_dict[key]} times.")
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words fount in the document.")

    for char, frequency in new_dict:
        printable_key = get_readable_char(char)
        print(f"The char '{printable_key}' was found {frequency} times.")
    

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def word_counter(input_text):
    counter = 0
    text_list = input_text.split()
    for word in text_list:
        counter += 1
    return counter

def char_counter(input_text):
    char_dict = {}
    for char in input_text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def char_dict_to_frequency_char_list(dict):
    temp_list = dict.items()
    new_temp_list = sorted(temp_list, key= lambda item: item[1], reverse=True)
    return new_temp_list

def get_readable_char(character):
    if character == " ":
        return "space"
    elif character == "\n":
        return "\\n"
    elif character == "\t":
        return "\\t"
    else:
        return character

main()