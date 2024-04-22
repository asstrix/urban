def print_params(a=1, b='string', c=True):
	print(a, b, c)


print_params()   								# Works
print_params(1)  								# Works
print_params(b='Hello')								# Works
print_params(1, 'Good bye')							# Works
print_params('Hello', c='Danil', b='My Name is')				# Works, as Python has dynamic typing
print_params(c=[1, 2, 3])							# Also workable, due to dynamic typing

values_list = [7.00000, 41560, 'Demo']
values_dict = {'a': 7.0, 'b': 41560, 'c': 'Demo'}
values_list2 = [7.01, True]
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 2, 42)						# Won't work as 4 parameters will be given
