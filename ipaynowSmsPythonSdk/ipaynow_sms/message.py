import urllib

from ipaynow_sms import interface
from pip._vendor import requests
from ipaynow_sms.error import APIInputError


def message(funcode, appId, appKey,desKey, mhtOrderNo, mobile,content, notifyUrl):
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
    resp = requests.post("https://sms.ipaynow.cn", messageStr)
    result = urllib.parse.unquote(resp.text)
    print(result)
    return1 = result.split("|")[0];
    if return1 == "0":
       return "fail"
    return2 = result.split("|")[1];
    return3 = result.split("|")[2];

    return
