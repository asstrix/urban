from pathlib import Path
import pandas as pd


class PriceMachine:
    
    def __init__(self):
        self.data = {}
        self.result = ''
        self.name_length = 0
    
    def load_prices(self, file_path=''):
        keyword = 'price'
        required_columns = [['товар', 'название', 'наименование', 'продукт'],
                            ['розница', 'цена'],
                            ['вес', 'масса', 'фасовка']]
        path = Path(file_path)
        for file in path.rglob('*'):
            if keyword in file.name:
                try:
                    df = pd.read_csv(file)
                    missing_columns = []
                    for i in required_columns:
                        if not any(col in df.columns for col in i):
                            missing_columns.append(i)
                    if not missing_columns:
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
print(pm.load_prices())

'''
    Логика работы программы
'''
# print('the end')
# print(pm.export_to_html())
