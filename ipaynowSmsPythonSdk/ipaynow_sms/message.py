import base64
import urllib
from _md5 import md5

from ipaynow_sms import interface
from ipaynow_sms.desUtil import desDecrypt, md5Encrypt
from pip._vendor import requests
from ipaynow_sms.error import APIInputError

proUrl = "https://sms.ipaynow.cn" #生产环境
testUrl = "https://dby.ipaynow.cn/sms" #测试环境


'''
 行业短信
 appId 商户应用Id 
 appKey 商户应用秘钥
 desKey des秘钥
 mhtOrderNo 商户订单号
 mobile 发送手机号 
 content 短信内容
 notifyUrl 后台通知地址
 isTest 是否测试 True 测试环境 False 生产环境
'''
def industryMessage(appId, appKey,desKey, mhtOrderNo, mobile,content, notifyUrl,isTest):
    return message("S01",appId, appKey,desKey, mhtOrderNo, mobile,content, notifyUrl,isTest)

'''
 营销短信
 appId 商户应用Id 
 appKey 商户应用秘钥
 desKey des秘钥
 mhtOrderNo 商户订单号
 mobile 发送手机号 
 content 短信内容
 notifyUrl 后台通知地址
 isTest 是否测试 True 测试环境 False 生产环境
'''
def salesMessage(appId, appKey,desKey, mhtOrderNo, mobile,content, notifyUrl,isTest):
    return message("YX_01",appId, appKey,desKey, mhtOrderNo, mobile,content, notifyUrl,isTest)


''' 
 短信查询   
 appId 商户应用Id 
 appKey 商户应用秘钥
 nowPayOrderNo 现在支付订单号
 mobile 手机号   
 isTest 是否测试 True 测试环境 False 生产环境
'''
def query(appId, appKey, nowPayOrderNo, mobile,isTest):
    paypara = {
        'funcode': "SMS_QUERY",
        'appId': appId,
        'nowPayOrderNo': nowPayOrderNo,
        'mobile': mobile,
    }
    messageStr = ""
    try:
        messageStr = interface.query(appKey, paypara)
    except APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    if isTest:
        url = testUrl
    else:
        url = proUrl
    resp = requests.post(url, messageStr)
    result = urllib.parse.unquote(resp.text)
    return result

def message(funcode, appId, appKey,desKey, mhtOrderNo, mobile,content, notifyUrl,isTest):
    paypara = {
        'funcode': funcode,
        'appId': appId,
        'mhtOrderNo': mhtOrderNo,
        'mobile': mobile,
        'content':content,
        'notifyUrl': notifyUrl,
    }
    messageStr = ""
    try:
        messageStr = interface.getMessageStr(appKey,desKey, paypara)
        messageStr = "funcode=" + funcode + "&message=" + messageStr
    except APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    if isTest:
        url = testUrl
    else:
        url = proUrl
    resp = requests.post(url, messageStr)
    result = urllib.parse.unquote(resp.text)
    return1 = result.split("|")[0];
    if return1 == "0":
       return "fail"
    return2 = result.split("|")[1];
    return3 = base64.b64decode(result.split("|")[2]);
    originalMsg = desDecrypt(desKey,return2.strip())
    sign = md5Encrypt(originalMsg + "&" + appKey)
    if str(return3,encoding="UTF-8") == sign:
        return originalMsg
    return "verfiy sign fail"

