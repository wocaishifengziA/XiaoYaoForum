# -*- coding:utf-8 -*-
__author__ = 'xiaoyao'
__date__ = '2019/5/20 22:21'
from XiaoYaoForm.settings import settings
from XiaoYaoForm.urls import urlpattern

from tornado import web
import tornado.options
from peewee_async import Manager
from XiaoYaoForm.settings import settings, database


if __name__ == "__main__":
    import wtforms_json
    wtforms_json.init()
    tornado.options.parse_command_line()

    app = web.Application(urlpattern, debug=True, **settings)

    objects = Manager(database)
    # No need for sync anymore!
    database.set_allow_sync(False)
    app.objects = objects

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
