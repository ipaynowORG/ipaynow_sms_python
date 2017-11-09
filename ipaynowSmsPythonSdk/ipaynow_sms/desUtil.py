# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
import base64
import binascii

from ipaynow_sms import pyDes

__all__ = ['StringIO', 'parse_qsl', 'desEncrypt','desDecrypt']



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

def encrypt(key, data):
    # iv = binascii.unhexlify(iv)
    hexKey = binascii.b2a_hex(key.encode())
    key = binascii.unhexlify(hexKey)
    k = pyDes.triple_des(key, pyDes.ECB, IV=None, pad=None, padmode=pyDes.PAD_NORMAL)
    d = k.encrypt(data)
    d = base64.encodestring(d)
    return d

def decrypt( key, data):
    hexKey = binascii.b2a_hex(key.encode())
    key = binascii.unhexlify(hexKey)
    k = pyDes.triple_des(key, pyDes.ECB, IV=None, pad=None, padmode=pyDes.PAD_NORMAL)
    data = base64.decodestring(data)
    d = k.decrypt(data)
    return d

def base64Encryt(str):
    return base64.encodebytes(binascii.b2a_hex(str.encode()))


#IV has to be 8bit long
iv = '2132435465768797'
#Key has to be 24bit long
key = 'hSbw2SwTFasdSdddnyS3sijv'


#here is the data you want to encrypt
data = "中午"

if __name__ == '__main__':
   # print (base64.b64encode('app'.encode(encoding="utf-8")))
   # print(base64Encryt("app"))
    # print(b'hSbw2SwTFasdSdddnyS3sijvarq')
    # print('hSbw2SwTFasdSdddnyS3sijvarq'.encode())
    # print(binascii.b2a_hex(u'hSbw2SwTFasdSdddnyS3sijv'.encode("utf8")))
    # print ("Plan Text: %s" % data)
   print( encryptdata = encrypt( key, data.encode()))
    # print ("Encrypted Text: %s" % encryptdata)
    # decryptdata = decrypt( key, encryptdata)
    # print ("Plan Text: %s" % decryptdata)

