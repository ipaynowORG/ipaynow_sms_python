#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
from ipaynow_sms.packMsg import PackMsgSend
from ipaynow_sms.paramlist import S01_PostList, SMS_QUERY_PostList

def getMessageStr(appKey,desKey,payparam = {}):
    pms = PackMsgSend(payparam["appId"],appKey,desKey,payparam,S01_PostList)
    return pms.getResultString()

def query(appKey,queryparam = {}):
    pms = PackMsgSend(appKey,queryparam,SMS_QUERY_PostList)
    return pms.getResultString()

def parseMessage(instr = ""):
    print(instr)
    return instr

def parseQuery(instr = ""):
    print(instr)
    return instr