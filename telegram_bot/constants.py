ACCESS_TOKEN = 'token'
DB_USER = 'user'
DB_PASSWORD = 'pass'
DB_HOST = 'host'
DB_PORT = 'port'
DB_DATABASE = 'db'


def get_db_connection_line():
    return f'pq://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
