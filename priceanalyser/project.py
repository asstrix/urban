from pathlib import Path
import pandas as pd


class PriceMachine:
    
    def __init__(self):
        self.data = {}
        self.result = ''
        self.name_length = 0
    
    def load_prices(self, file_path=''):
        keyword = 'price'
        required_columns = [['наименование','товар', 'название', 'продукт'],
                            ['цена','розница'],
                            ['вес', 'масса', 'фасовка']]
        path = Path(file_path)
        for file in path.rglob('*'):
            if keyword in file.name:
                try:
                    df = pd.read_csv(file)
                    rubbish = [i for i in df.columns if i not in [j for k in required_columns for j in k]]
                    df = df.drop(columns=rubbish).dropna(axis=1, how='all')
                    rename_map = {}
                    missing_columns = []
                    for i in required_columns:
                        found_column = next((col for col in df.columns if col in i), None)
                        if found_column:
                            standard_name = i[0]
                            rename_map[found_column] = standard_name
                        else:
                            missing_columns.append(i)
                    if not missing_columns:
                        df = df.rename(columns=rename_map)
                        df = df[[i[0] for i in required_columns]]
                        df['файл'] = file.name
                        df['цена за кг.'] = round(df['цена']/df['вес'], 1)
                        self.data[file.name] = df
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
