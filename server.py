# -*- coding:utf-8 -*-
from XiaoYaoForm import settings
from XiaoYaoForm.urls import urlpattern

__author__ = 'xiaoyao'
__date__ = '2019/5/20 22:21'

from tornado import web
import tornado
import tornado.options


class MainHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello world2")

    def post(self):
        self.write


urls = [
    ("/", MainHandler),
]

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = web.Application(urlpattern, debug=True, **settings)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    # print('ok')
