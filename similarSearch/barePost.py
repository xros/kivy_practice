#!/usr/bin/env python
#coding=utf8

import httplib, urllib

httpClient = None
try:
    params = urllib.urlencode({'username': 'admin', 'password': "default"})
    headers = {"Content-type": "application/x-www-form-urlencoded" \
                    , "Accept": "text/plain"}

    httpClient = httplib.HTTPConnection("localhost", port=5000, timeout=30)
    httpClient.request("POST", "/login", params, headers)

    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() #获取头信息
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()