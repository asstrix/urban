import json
from pprint import pprint


def employees_rewrite(sort_type):
	with open('employees.json', 'r') as f_in, open(f' employees_{sort_type}_sorted.json', 'w', encoding='utf-8') as f_out:
		data = json.load(f_in)
		if sort_type.lower() in [i.lower() for i in data['employees'][0].keys()]:
			sorted_data = sorted(data['employees'], key=lambda x: x[sort_type])
			json.dump(sorted_data, f_out, ensure_ascii=False, indent=4)
		else:
			raise ValueError('Bad key for sorting')


employees_rewrite('salary')
employees_rewrite('department')
employees_rewrite('lastName')
employees_rewrite('firstName')
