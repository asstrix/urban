import csv


def write_holiday_cities(first_letter):
	visited = set()
	visit = set()
	with open('travel-notes.csv', 'r') as f_in, open('holiday.csv', 'w', encoding='utf-8') as f_out:
		file = csv.reader(f_in, delimiter=',')
		for row in file:
			if row[0].startswith(first_letter):
				visited.update(row[1].split(';'))
				visit.update(row[2].split(';'))
		not_visited = visit.difference(visited)
		f_out.write(f"Have visited: {', '.join(sorted(list(visited)))}" + '\n')
		f_out.write(f"Want to visit: {', '.join(sorted(list(visit)))}" + '\n')
		f_out.write(f"No one has been to: {', '.join(sorted(list(not_visited)))}" + '\n')
		f_out.write(f"In the end, we will go to: {sorted(list(not_visited))[0]}")


write_holiday_cities('L')