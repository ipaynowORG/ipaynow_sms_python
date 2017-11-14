# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
import base64
import binascii
import hashlib
import urllib
from urllib.parse import quote

from ipaynow_sms import pyDes

__all__ = ['StringIO', 'parse_qsl', 'desEncrypt', 'desDecrypt']

try:
    # When cStringIO is available
    import cStringIO as StringIO
except ImportError:
    from io import StringIO

try:
    from urlparse import parse_qsl
except ImportError:
    # Python < 2.6
    from cgi import parse_qsl


def desEncrypt(key, data):
    # iv = binascii.unhexlify(iv)
    hexKey = binascii.b2a_hex(key.encode())
    key = binascii.unhexlify(hexKey)
    k = pyDes.triple_des(key, pyDes.ECB, IV=None, pad=None, padmode=pyDes.PAD_NORMAL)
    d = k.encrypt(complementZero(data),pad="0",padmode=pyDes.PAD_NORMAL)
    r = base64.encodestring(d)
    r = r.strip(b'\n').replace(b'\n',b'')
    return r


def desDecrypt(key, data):
    hexKey = binascii.b2a_hex(key.encode())
    key = binascii.unhexlify(hexKey)
    k = pyDes.triple_des(key, pyDes.ECB, IV=None, pad=None, padmode=pyDes.PAD_NORMAL)
    dataByte1 = base64.b64decode(data.encode())
    d = k.decrypt(dataByte1,pad=None,padmode=pyDes.PAD_NORMAL).strip(b'\x00')
    re = str(d,encoding="UTF-8")
    return re


def base64Encryt(str):
    return base64.encodebytes(binascii.b2a_hex(str.encode()))


def md5Encrypt(src):
    m2 = hashlib.md5()
    m2.update(src.encode())
    return m2.hexdigest()

'''
字符串字节码补全
'''
def complementZero(data):
    dataByte = bytes(data,encoding="UTF-8")
    array = bytearray(dataByte)
    len1 = dataByte.__len__() - dataByte.__len__() % 8 + 8
    len2 = (len1 - dataByte.__len__())
    if dataByte.__len__() % 8 == 0:
        return dataByte
    else:
        for i in range (0,len2):
            array.append(0x00)
        b = bytes(array)
        return b

def complementZeroB(data):
    # dataByte = bytes(data, encoding="UTF-8")
    #dataByte1 = base64.b64decode(data.encode())
    array = bytearray(data)
    len1 = data.__len__() - data.__len__() % 8 + 8
    len2 = (len1 - data.__len__())
    if data.__len__() % 8 == 0:
        return data
    else:
        for i in range(0, len2):
            array.append(0x00)
        b = bytes(array)
        return b

# IV has to be 8bit long
iv = '2132435465768797'
# Key has to be 24bit long
key = 'hSbw2SwTFasdSdddnyS3sijv'

# here is the data you want to encrypt
data = "appId=150753086263684&content=python1&funcode=S01&mhtOrderNo=industry2&mobile=17701087752&notifyUrl=https://op-tester.ipaynow.cn/paytest/notify"


code = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encodeBase64(src, encode="utf-8"):
    global code

    paddingTail = {0: '', 8: '0000', 16: '00'}
    paddingEqual = {0: '', 8: '==', 16: '='}

    src = src.encode(encode)
    sin = ''
    for c in src:
        sin += bin(c)[2:].zfill(8)
    n = len(sin) % 24
    sin += paddingTail[n]

    output = ''
    for i in range(6, len(sin) + 1, 6):
        output += code[int(sin[i - 6:i], 2)]
    output += paddingEqual[n]

    return output


def decodeBase64(src, encode="utf-8"):
    global code
    delPaddingTail = {0: 0, 2: 4, 1: 2}

    value = ''
    n = src.count('=')
    sin = src[:len(src) - n]
    for c in sin:
        value += bin(code.find(c))[2:].zfill(6)
    value = value[:len(value) - delPaddingTail[n]]

    middle = []
    for i in range(8, len(value) + 1, 8):
        middle.append(int(value[i - 8:i], 2))
    output = bytes(middle).decode(encoding=encode)

    return output


if __name__ == '__main__':
    s = md5Encrypt("appId=150753086263684&funcode=SMS_QUERY&mobile=17701087752&nowPayOrderNo=400001201711141621592425552&zHGKLmQaU9PLMEGObyubsV5uhDAeYVqQ")
    print(s)
    # print('hSbw2SwTFasdSdddnyS3sijvarq'.encode())
    # print(binascii.b2a_hex(u'hSbw2SwTFasdSdddnyS3sijv'.encode("utf8")))
    # print ("Plan Text: %s" % data)
    # encryptdata = desEncrypt("a8ifp3YwBSjipz3BisGA8akF"[:24], "appId=150753086263684&content=python测试&funcode=S01&mhtOrderNo=industry2&mobile=17701087752&notifyUrl=www.baidu.com")
    # print ("Encrypted Text: %s" % encryptdata)
    # print(base64.urlsafe_b64decode("wZsv7Ak9CUaYXX9eJNn2XpyAutksVIxrCUdZ8MN41+PqvrsOKopO2QSvmENG/NRlWdGITGR0k6ZD6Gh/dBbnyqnh59AatePktfhmP/liJLYynPP0bvNP7UnoatLwyFSuH7CnjcLGOEmDjtWP3ze5KvAbmrX1PyXmOQFqkloqeNScryBTu+y+Obf9tTJ4EcUtRlAFeExVe5w="))
    # baes = base64.urlsafe_b64decode()

    # decryptdata = desDecrypt( "a8ifp3YwBSjipz3BisGA8akF","nb+Io747oF8jE4jpi+rxKPpUEyDGSC9ylfacyHEohp/h1gpP+aOHCcd+BrJx4ajasGoVRn68hP6TrfHI7hgn+ChqP+bO701rjl0FLhztwr0BUWudqwKVGRWUPLPcwkKJ95mrRtsPEYil7OPDpLAvkoQfhn5/GEo3q2ARnbNHOaoW8HQZbspChjzwN0UgBQJEqCSWWWqv9uQ=")
    # print(decryptdata)
    # b = base64.urlsafe_b64encode("funcode=S01&mhtOrderNo=industry4&nowpayTransId=400001201711131022362364123&responseCode=00&responseMsg=success&responseTime=20171113102236&status=00".encode())
    # print( (b))
    # a = base64.b64decode("nb+Io747oF8jE4jpi+rxKPpUEyDGSC9ylfacyHEohp/h1gpP+aOHCcd+BrJx4ajasGoVRn68hP6TrfHI7hgn+ChqP+bO701rjl0FLhztwr0BUWudqwKVGRWUPLPcwkKJ95mrRtsPEYil7OPDpLAvkoQfhn5/GEo3q2ARnbNHOaoW8HQZbspChjzwN0UgBQJEqCSWWWqv9uQ=",altchars="-_",validate=True)
    # print(str(a,encoding="UTF-8"))

    # print(encodeBase64("funcode=S01&mhtOrderNo=industry4&nowpayTransId=400001201711131022362364123&responseCode=00&responseMsg=success&responseTime=20171113102236&status=00"))
    #
    # print(decodeBase64("ZnVuY29kZT1TMDEmbWh0T3JkZXJObz1pbmR1c3RyeTQmbm93cGF5VHJhbnNJZD00MDAwMDEyMDE3MTExMzEwMjIzNjIzNjQxMjMmcmVzcG9uc2VDb2RlPTAwJnJlc3BvbnNlTXNnPXN1Y2Nlc3MmcmVzcG9uc2VUaW1lPTIwMTcxMTEzMTAyMjM2JnN0YXR1cz0wMA=="))
    # print ("Plann Text: %s" % decryptdata)



