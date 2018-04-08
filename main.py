#!/usr/bin/python
# -*- coding: utf8 -*-

from urllib.request import Request, urlopen
from urllib.parse import urlencode


def get_short_url(long_url):
    data = urlencode({
        "url": long_url,
        "format": "simple"
    })
    req = Request(
        url="https://qwqq.pw/api.php",
        method="POST",
        data=bytes(data, 'utf8')
    )
    with urlopen(req, timeout=60) as res:
        print(str(res.read(), 'utf8'))


if __name__ == '__main__':
    get_short_url("https://www.baidu.com")
