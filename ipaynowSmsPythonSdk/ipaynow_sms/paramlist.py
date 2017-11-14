#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4

# define interface parameter attributes and max len

# key name 'name' indicates parameter name
# key name 'must' indicates parameter
# 行业短信
S01_PostList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 5, 'desp': "功能码"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户订单号"},
    {'name': 'mobile', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "手机号"},
    {'name': 'content', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 1000, 'desp': "短信内容"},
    {'name': 'notifyUrl', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "通知地址"}
]


# 营销短信
YX_01_PostList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 5, 'desp': "功能码"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'mhtOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户订单号"},
    {'name': 'mobile', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "手机号"},
    {'name': 'content', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 1000, 'desp': "短信内容"},
    {'name': 'notifyUrl', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 64, 'desp': "通知地址"}
]



# 查询接口
SMS_QUERY_PostList = [
    {'name': 'funcode', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 9, 'desp': "功能码"},
    {'name': 'appId', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "商户应用唯一标识"},
    {'name': 'nowPayOrderNo', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 40, 'desp': "现在支付订单号"},
    {'name': 'mobile', 'mandatory': 'Y', 'md5': 'Y', 'type': 'str', 'len': 11, 'desp': "手机号"},
    {'name': 'mchSign', 'mandatory': 'N', 'md5': 'N', 'type': 'str', 'len': 32, 'desp': "商户签名"}
]
