import requests as rq, logging, os


class Logger:
    def __init__(self, name, level, log_file):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.FileHandler(log_file, 'w', encoding='utf-8')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def log(self, level, message):
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'error':
            self.logger.error(message)


if not os.path.exists('../RequestsLogger/logs'):
    os.makedirs('../RequestsLogger/logs')

# Create objects for each type of logging
success = Logger('success', logging.INFO, '../RequestsLogger/logs/success_responses.log')
bad = Logger('bad', logging.DEBUG, '../RequestsLogger/logs/bad_responses.log')
blocked = Logger('blocked', logging.ERROR, '../RequestsLogger/logs/blocked_responses.log')

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        print(response.status_code)
        if response.status_code == 200:
            success.log('info', f'{site}')
        elif response.status_code == 503:
            bad.log('debug', f'{site}')
        elif response.status_code == 403:
            blocked.log('error', f'{site}')
    except rq.exceptions.RequestException as e:
        bad.log('error', f'Error accessing {site}: {e}')