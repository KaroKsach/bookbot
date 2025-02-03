from typing import Dict


def main():
    path_to_file = "./books/frankenstein.txt"
    num_words_in_book = 0
    with open(path_to_file) as f:
        file_contents = f.read()
    char_dict = count_characters(file_contents)
    num_words = word_count(file_contents)
    print_report(char_dict, num_words, path_to_file)
        # print(file_contents)
        # words = file_contents.split()
        # num_words_in_book = len(words)
        # print(num_words_in_book)
    
def count_characters(file_contents: str):
    
    char_dict = {}

    for char in file_contents:
        if not char.lower() in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    return char_dict
def word_count(file_contents: str,):
    words = file_contents.split()
    num_words_in_book = len(words)
    return num_words_in_book
def print_report(char_dict: Dict, word_count: int,  path_to_file: str):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    for item in char_dict:
        if item.isalpha():
            print(f"The '{item}' character was found {char_dict[item]} times")

main()