from pathlib import Path
import pandas as pd


class PriceMachine:
    
    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

    # def load_prices(self, file_path=''):
    #     keyword = 'price'
    #     required_columns = [['наименование','товар', 'название', 'продукт'],
    #                         ['цена','розница'],
    #                         ['вес', 'масса', 'фасовка']]
    #     path = Path(file_path)
    #     first_file = True
    #     for file in path.rglob('*'):
    #         if keyword in file.name:
    #             try:
    #                 if first_file:
    #                     df = pd.read_csv(file)
    #                     first_file = False
    #                 else:
    #                     df = pd.read_csv(file, header=None, skiprows=1)
    #                 rubbish = [i for i in df.columns if i not in [j for k in required_columns for j in k]]
    #                 df = df.drop(columns=rubbish).dropna(axis=1, how='all')
    #                 rename_map = {}
    #                 missing_columns = []
    #                 for i in required_columns:
    #                     found_column = next((col for col in df.columns if col in i), None)
    #                     if found_column:
    #                         standard_name = i[0]
    #                         rename_map[found_column] = standard_name
    #                     else:
    #                         missing_columns.append(i)
    #                 if not missing_columns:
    #                     df = df.rename(columns=rename_map)
    #                     df = df[[i[0] for i in required_columns]]
    #                     df['файл'] = file.name
    #                     df['цена за кг.'] = round(df['цена']/df['вес'], 1)
    #                     self.data.append(df)
    #                 if self.data:
    #                     self.data = pd.concat(self.data, ignore_index=True)
    #             except Exception as e:
    #                 print(f"Error processing file {file}: {e}")
    #     return self.data

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
                    correct_order = [col_group[0] for col_group in required_columns]
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
