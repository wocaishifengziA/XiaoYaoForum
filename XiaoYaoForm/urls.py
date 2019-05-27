from tornado.web import url, StaticFileHandler

from XiaoYaoForm.settings import settings
from apps.users import urls as user_urls
from apps.community import urls as community_urls
from apps.ueditor import urls as ueditor_urls
from apps.question import urls as question_urls

urlpattern = [
    (url("/media/(.*)", StaticFileHandler, {'path': settings["MEDIA_ROOT"]})),
]
urlpattern += user_urls.urlpattern
urlpattern += community_urls.urlpattern
urlpattern += ueditor_urls.urlpattern
urlpattern += question_urls.urlpattern
