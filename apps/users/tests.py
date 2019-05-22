import json

import requests

web_url = "http://127.0.0.1:8888"


def test_sms():
    url = "{}/code/".format(web_url)
    data = {
        "mobile": "18782651256"
    }
    res = requests.post(url, json=data)

    print(json.loads(res.text))
