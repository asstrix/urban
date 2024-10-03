from pathlib import Path
import pandas as pd


class PriceMachine:
    
    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

    def load_prices(self, file_path=''):
        keyword = 'price'
        required_columns = [
            ['наименование', 'товар', 'название', 'продукт'],
            ['цена', 'розница'],
            ['вес', 'масса', 'фасовка']
        ]
        path = Path(file_path)
        first_file = True
        for file in path.rglob('*'):
            if keyword in file.name:
                try:
                    df = pd.read_csv(file)
                    valid_columns = [col for sublist in required_columns for col in sublist]
                    df = df[[col for col in df.columns if col in valid_columns]].dropna(axis=1, how='all')
                    rename_map = {}
                    for i in required_columns:
                        column_found = next((col for col in df.columns if col in i), None)
                        if column_found:
                            rename_map[column_found] = i[0]
                    df = df.rename(columns=rename_map)
                    if not all([i[0] in df.columns for i in required_columns]):
                        print(f"File {file} skipped: required columns are absent")
                        continue
                    correct_order = [i[0] for i in required_columns]
                    if list(df.columns[:3]) != correct_order:
                        df = df[correct_order + list(df.columns[3:])]
                    df['файл'] = file.name
                    df['цена за кг.'] = round(df['цена'] / df['вес'], 1)
                    if first_file:
                        self.data = df
                        first_file = False
                    else:
                        self.data = pd.concat([self.data, df], ignore_index=True)
                except Exception as e:
                    print(f"Error processing file {file}: {e}")
        return self.data

    def _search_product_price_weight(self, headers):
        '''
            Возвращает номера столбцов
        '''

    def export_to_html(self, fname='output.html'):
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''
    
    # def find_text(self, text):

    
pm = PriceMachine()
# pm.load_prices()
print(pm.load_prices())

'''
    Логика работы программы
'''
# print('the end')
# print(pm.export_to_html())
