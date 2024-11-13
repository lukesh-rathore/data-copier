import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '24.190.57.247',
            'DB_NAME': os.environ.get('SOURCE_DB_NAME'),
            'DB_USER': os.environ.get('SOURCE_DB_USER'),
            'DB_PASS': os.environ.get('SOURCE_DB_PASS'),
        },
        'TARGET_DB': {
            'DB_TYPE': 'sqlserver',
            'DB_HOST': os.environ.get('COMPUTERNAME'), #'DESKTOP-KS52KPT',
            'DB_NAME': os.environ.get('TARGET_DB_NAME'),
        }
    }
}