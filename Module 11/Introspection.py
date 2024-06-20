import inspect


class Phone:
	def __init__(self, model, os):
		self.model = model
		self.os = os

	def func(self):
		def func2():
			pass
		return func2


def introspection_info(obj):
	dict_ = dict()
	dict_['type'] = str(type(obj)).split(' ')[1].strip("'>")
	dict_['attr'] = dir(obj)[:2] if len(dir(obj)) > 2 else dir(obj)
	dict_['methods'] = [name for name, value in inspect.getmembers(obj) if callable(value) and not name.startswith('__')]
	try:
		dict_['module'] = str(inspect.getmodule(obj)).split(' ')[1].strip("'")
	except Exception:
		dict_['module'] = ''
	return dict_


phone1 = Phone('Sony', 'Android')
print(introspection_info(phone1))