import string


def ask_text():
    text = input("Enter a string: ")
    return text


def ask_text2_for_anagram():
    text2 = input("Enter a string: ")
    return text2


def is_palindrome(text):
    text_1 = text.lower()
    only_letters = ""
    for le in text_1:
        if le.isalpha():
            only_letters += le
    if only_letters == only_letters[::-1]:
        return True
    else:
        return False


def is_isogram(text):
    text = text.lower()
    o_letters = ""
    for letters in text:
        if letters.isalpha():
            o_letters += letters
    for elements in o_letters:
        letter_counter = o_letters.count(elements)
        if letter_counter > 1:
            return False
        else:
            return True


def is_anagram(text, text2):
    text = text.lower()
    text2 = text2.lower()
    final_text1 = ""
    for i in text:
        if i.isalpha():
            final_text1 = final_text1 + i
    final_text2 = ""
    for char in text2:
        if char.isalpha():
            final_text2 = final_text2 + char
    if set(final_text1) == set(final_text2):
        return True
    else:
        return False


def is_pangram(text):
    text = text.lower()
    text_w_n_letters = ""
    for le in text:
        if le.isalpha():
            text_w_n_letters += le
    alphabet = string.ascii_lowercase
    for i in alphabet:
        if i not in text_w_n_letters:
            return False
    return True

