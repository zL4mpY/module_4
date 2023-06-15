str_ = input('Введите строку: ')
reverse_str = ""

for char in reversed(str_):
	reverse_str += char

if str_ == reverse_str:
	print(True)

else:
	print(False)