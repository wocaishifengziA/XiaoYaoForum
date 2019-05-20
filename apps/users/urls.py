from tornado.web import url


urlpattern = (
    url("/login/", LoginHandler)
)