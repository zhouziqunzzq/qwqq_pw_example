#!/usr/bin/python
# -*- coding: utf8 -*-

import requests


def get_short_url(long_url):
    data = {
        "url": long_url,
        "format": "simple"
    }
    r = requests.post("https://qwqq.pw/api.php", data)
    return r.text


if __name__ == '__main__':
    print(get_short_url("https://www.baidu.com"))
