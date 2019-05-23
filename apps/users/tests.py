import json

import requests

web_url = "http://127.0.0.1:8888"
def test_sms():
    url = "{}/code/".format(web_url)
    data = {
        "mobile": "18782651256"
    }
    res = requests.post(url, json=data)

    print(res.text)

def test_register():
    url = "{}/register/".format(web_url)
    data = {
        "mobile": "18782651256",
        "code": "1234",
        "password": "admin123"
    }
    res = requests.post(url, json=data)

    print(json.loads(res.text))

def test_login():
    # url = "{}/login/".format(web_url)
    url = "http://127.0.0.1:8888/login/"
    data = {
        "mobile": "18782651256",
        "password": "admin123"
    }
    res = requests.post(url, json=data)

    print(json.loads(res.text))


if __name__ == "__main__":
    # test_sms()
    # test_register()
    test_login()