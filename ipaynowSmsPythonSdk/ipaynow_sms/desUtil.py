# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
import base64
import binascii
import hashlib
from _md5 import md5

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
    d = base64.encodestring(d)
    return d


def desDecrypt(key, data):
    hexKey = binascii.b2a_hex(key.encode())
    key = binascii.unhexlify(hexKey)
    k = pyDes.triple_des(key, pyDes.ECB, IV=None, pad=None, padmode=pyDes.PAD_NORMAL)
    d = k.decrypt(complementZeroB(data),pad="0",padmode=pyDes.PAD_NORMAL)
    # r = str(d)
    r = bytes.decode(d)
    # r = d.decode("UTF-8")
    return r


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

if __name__ == '__main__':
    # print(complementZero(data))
    # print(md5("中".encode()))
    # print (base64.b64encode('app'.encode(encoding="utf-8")))
    # print(base64Encryt("app"))
    # print(b'hSbw2SwTFasdSdddnyS3sijvarq')
    # print('hSbw2SwTFasdSdddnyS3sijvarq'.encode())
    # print(binascii.b2a_hex(u'hSbw2SwTFasdSdddnyS3sijv'.encode("utf8")))
    # print ("Plan Text: %s" % data)
    # encryptdata = desEncrypt(key, data)
    # print ("Encrypted Text: %s" % encryptdata)
    # b = base64.b64decode("ztLKx9fWt/u0rg==")
    # print(b)
    # str = "nb+Io747oF85e0G5u6wfbKU8Tiu0Ry8BAZdw+772u7AkMoSNYzv0q/TgRJcuxuGZbV2+bAERP3Dpq+A5yAc1nYQfhn5/GEo3q2ARnbNHOaq2fzYTS32fNV/oaD/Txyk5".replace(
    #     "+", "").replace("/", "")
    # print(str)
    # baes = base64.urlsafe_b64decode()
    # decryptdata = desDecrypt( key,baes)

    b = base64.b64encode("funcode=S01&responseCode=01&responseMsg=商户订单号重复!&responseTime=20171110182013 ".encode())
    print(b)
    a = base64.b64decode(b)
    print(str(a))

    # print ("Plann Text: %s" % decryptdata)
