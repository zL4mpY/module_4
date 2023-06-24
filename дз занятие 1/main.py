def is_palindrom(str_):
    str_ = str_.lower()
    reverse_str = ""
    for char in reversed(str_):
        reverse_str += char

    if str_ == reverse_str:
        return True

    else:
        return False

print(is_palindrom(input('Введите строку: ')))
