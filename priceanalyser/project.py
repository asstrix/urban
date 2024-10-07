from pathlib import Path
import pandas as pd
import shutil, os


class PriceMachine:

	def __init__(self):
		self.data = pd.DataFrame()
		self.result = pd.DataFrame()
		self.path = Path(__file__).parent

	def __str__(self):
		if not self.result.empty:
			if os.name == 'nt':
				os.system('cls')
			else:
				os.system('clear')
			# Count max len of values to set len of header
			col_widths = [max(len(str(val)) for val in self.result[col]) for col in self.result.columns]
			col_widths = [max(len(col), width) for col, width in zip(self.result.columns, col_widths)]
			header = self.result.columns[0].ljust(col_widths[0]) + "  " + "  ".join(
				[self.result.columns[i].center(col_widths[i]) for i in range(1, len(self.result.columns))]
			)
			print(header)
			for _, row in self.result.iterrows():
				row_str = str(row.iloc[0]).ljust(col_widths[0]) + "  " + "  ".join(
					[str(row.iloc[i]).center(col_widths[i]) for i in range(1, len(row))]
				)
				print(row_str)
		return ''

	def load_prices(self):
		keyword = 'price'
		required_columns = [
			['наименование', 'товар', 'название', 'продукт'],
			['цена', 'розница'],
			['вес', 'масса', 'фасовка']
		]
		first_file = True
		for file in self.path.rglob('*'):
			if keyword in file.name:
				try:
					df = pd.read_csv(file)
					valid_columns = [col for col_list in required_columns for col in col_list]
					df = df[[col for col in df.columns if col in valid_columns]].dropna(axis=1, how='all')
					rename_map = {}
					for i in required_columns:
						column_found = next((col for col in df.columns if col in i), None)
						if column_found:
							rename_map[column_found] = i[0]
					df = df.rename(columns=rename_map)
					if not all([i[0] in df.columns for i in required_columns]):
						# print(f"File {file} skipped: required columns are absent")
						continue
					correct_order = [i[0] for i in required_columns]
					if list(df.columns[:3]) != correct_order:
						df = df[correct_order + list(df.columns[3:])]
					df['файл'] = file.name
					df['цена за кг.'] = round(df['цена'] / df['вес'], 2)
					if first_file:
						self.data = df
						first_file = False
					else:
						self.data = pd.concat([self.data, df], ignore_index=True)
				except Exception as e:
					print(f"Error processing file {file}: {e}")
		return self.data

	def find_text(self, key_phrase):
		if self.data.empty:
			print("Data not loaded.")
			return pd.DataFrame()
		self.result = self.data[self.data[self.data.columns[0]].str.contains(key_phrase, case=False, na=False)]
		if not self.result.empty:
			self.result = self.result.sort_values(by=self.result.columns[-1], ascending=True).reset_index(drop=True)
			self.result = self.result.reset_index()
			self.result.rename(columns={'index': '№'}, inplace=True)
			self.result['№'] = self.result['№'] + 1
			return self.result
		else:
			print(f"No matches with '{key_phrase}' were found.")
			return pd.DataFrame()

	def export_to_html(self, fname='output.html'):
		self.result = self.result.sort_values(by=self.data.columns[-1], ascending=True).reset_index(drop=True)
		self.result = self.result.reset_index(drop=True)
		self.result.rename(columns={'№': 'номер'}, inplace=True)
		self.result['номер'] = self.result['номер']
		table = self.result.to_html(index=False, border=0)
		result = '''
		<!DOCTYPE html>
		<html>
		<head>
			<title>Позиции продуктов</title>
			<style>
                table {width: 30%; border-collapse: collapse;}
                th, td {padding: 8px; line-height: 0.5;}
                th {text-align: center;}
                td:nth-child(2) {text-align: left;}
                td {text-align: center;}
            </style>
		</head>
		<body>
			<div>
				{{table}}
			</div>
   		 </body>
		</html>
		'''
		html = result.replace('{{table}}', table)
		try:
			with open(self.path/fname, 'w', encoding='utf-8') as file:
				file.write(html)
			print(f"The data has been successfully saved to {self.path/fname}")
		except Exception as e:
			print(f"Error saving to HTML: {e}")


pm = PriceMachine()
pm.load_prices()
terminal_size = shutil.get_terminal_size(fallback=(80, 20))
width = terminal_size.columns
text = """
Welcome to PriceMachine
Please make sure that you placed files or catalog of files to the same folder of the app
In order to export all files to one html file type 'export'
In order to close the app type 'exit'
"""
print("\n".join(line.center(width) for line in text.strip().splitlines()))

while True:
	text = input('Enter the search word:\n')
	if text == 'exit':
		print('Thank you for using our app')
		break
	elif text == 'export':
		pm.export_to_html()
	else:
		pm.find_text(text)
		print(pm)
