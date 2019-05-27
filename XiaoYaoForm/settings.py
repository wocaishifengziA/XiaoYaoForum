import os

import peewee_async
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
settings = {
    "secret_key": "ZGGA#Mp4yL4w5CDu",
    "redis": {
        "host": "127.0.0.1",
        "port": 6379,
        "password": "deng"
    },
    "MEDIA_ROOT": os.path.join(BASE_DIR, "media"),
    "jwt_expire": 7 * 24 * 3600,
    "SITE_URL": "http://127.0.0.1:8888",
}

database = peewee_async.MySQLDatabase(
    'xyforum', host="118.24.115.8", port=3306, user="root", password="123456"
)