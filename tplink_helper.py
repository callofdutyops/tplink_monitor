#!/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import sys

progArgs = ["get_status", "login"]

ip = "192.168.0.1"

headers = {
    "Host": "192.168.0.1",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/65.0.3325.181 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "http://192.168.0.1/userRpm/StatusRpm.htm",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,bg;q=0.6,la;q=0.5",
    "Cookie": "Authorization=*你的authorization值*"
}

statusUrl = "http://" + ip + "/userRpm/StatusRpm.htm"

loginUrl = "http://" + ip + "/userRpm/WanCfgRpm_8021X.htm" \
                            "?wantype=3" \
                            "&Ieee802_1xName=*你的宽带账户*" \
                            "&Ieee802_1xPwd=Hello123World" \
                            "&dialMode=2" \
                            "&Login=%B5%C7+%C2%BC&IpType=1" \
                            "&sta_ip=" \
                            "&sta_mask=" \
                            "&sta_gateway=" \
                            "&mtu=1500" \
                            "&ieeeType=3"
#logoutUrl = "http://" + ip + "/userRpm/StatusRpm.htm?Logout=%CD%CB%20%B3%F6&wan=1"
logoutUrl = "http://" + ip + "/userRpm/WanCfgRpm_8021X.htm" \
                             "?wantype=3" \
                             "&Ieee802_1xName=*你的宽带账户*" \
                             "&Ieee802_1xPwd=Hello123World" \
                             "&Logout=%CD%CB+%B3%F6" \
                             "&IpType=1" \
                             "&sta_ip=" \
                             "&sta_mask=" \
                             "&sta_gateway=" \
                             "&mtu=1500" \
                             "&ieeeType=3" \
                             "&IeeeReqFlag=0"


def get_url(url_arg):
    if url_arg == "get_status":
        req = urllib.request.Request(statusUrl, None, headers)
    elif url_arg == "login":
        //先登出，再登入，防止特殊情况
        req = urllib.request.Request(logoutUrl, None, headers)
        req = urllib.request.Request(loginUrl, None, headers)
    else:
        # default, should never reach here
        req = urllib.request.Request(statusUrl, None, headers)
    resp = urllib.request.urlopen(req)
    print(resp.read())


def print_help():
    base_help_str = "Usage: " + sys.argv[0] + " "
    print(base_help_str + "|".join(progArgs))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in progArgs:
        print_help()
        exit(1)
    else:
        get_url(sys.argv[1])

