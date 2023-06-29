def is_palindrom(word):
    word = word.lower()
    reversed_word = ""
    for char in reversed(word):
        reversed_word += char
    
    if word == reversed_word:
        return True

    else:
        return False

print(is_palindrom(input('Введите строку: ')))
