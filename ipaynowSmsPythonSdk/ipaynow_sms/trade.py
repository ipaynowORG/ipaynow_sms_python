import urllib

from ipaynowSmsPythonSdk.ipaynow_sms import interface
from pip._vendor import requests


def message(funcode, appId, appKey, mhtOrderNo, mobile, notifyUrl):
    paypara = {
        'funcode': funcode,
        'appId': appId,
        'mhtOrderNo': mhtOrderNo,
        'mobile': mobile,
        'notifyUrl': notifyUrl,
    }
    try:
        tradestr = interface.getMessageStr(appKey, paypara)
    except interface.APIInputError as ipse:
        print(ipse)
    except Exception as e:
        print(e)
        print(e.with_traceback)
    resp = requests.post("https://pay.ipaynow.cn", tradestr)
    return urllib.parse.unquote(resp.text)
