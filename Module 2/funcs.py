phrase = 'Я банан'
def print_param(param):
	if ' ' in param and len(param.split(' ')) == 2 and len(param.split(' ')[1]) > 4:
		print(' '.join([param[0] for i in range(2)]))
		print(' '.join([param[0] for i in range(2)]), ' '.join([param[-5:] for i in range(2)]))
	else:
		print(param)
		print(' '.join([param for i in range(1)]))
print_param('Я банан')
print_param('ха ха')