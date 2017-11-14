#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
from ipaynowSmsPythonSdk.ipaynow_sms.message import message, industryMessage, salesMessage, query

# print(message("S01","150753086263684","zHGKLmQaU9PLMEGObyubsV5uhDAeYVqQ","a8ifp3YwBSjipz3BisGA8akF","industry2","17701087752","python测试","www.baidu.com"))

# print(industryMessage("150753086263684","zHGKLmQaU9PLMEGObyubsV5uhDAeYVqQ","a8ifp3YwBSjipz3BisGA8akF","industry22","17701087752","python1","https://op-tester.ipaynow.cn/paytest/notify"))

# print(salesMessage("150753086263684","zHGKLmQaU9PLMEGObyubsV5uhDAeYVqQ","w75zriHtT85zpCYW3y8Dpw2k","pythonsales2","17701087752","python营销短信测试","https://op-tester.ipaynow.cn/paytest/notify"))

print(query("150753086263684","zHGKLmQaU9PLMEGObyubsV5uhDAeYVqQ","400001201711141621592425552","17701087752"))