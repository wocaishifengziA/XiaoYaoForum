import peewee_async

settings = {
    "redis": {
        "host": "127.0.0.1",
        "port": 6379,
    },
}

database = peewee_async.MySQLDatabase(
    'xyforum', host="118.24.115.8", port=3306, user="root", password="123456"
)