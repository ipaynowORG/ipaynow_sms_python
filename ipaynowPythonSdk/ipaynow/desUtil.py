# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
import base64
import os
import io
import string
import sys

import binascii

from ipaynowPythonSdk.ipaynow import pyDes

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



def desEncrypt(key,value):
   print(key)

def desDecrypt(key,value):
    print(key)

def encrypt(key, data):
    # iv = binascii.unhexlify(iv)
    key = binascii.unhexlify(key)
    k = pyDes.triple_des(key, pyDes.ECB, IV=None, pad=None, padmode=pyDes.PAD_NORMAL)
    d = k.encrypt(data)
    d = base64.encodestring(d)
    return d

def decrypt( key, data):
    key = binascii.unhexlify(key)
    k = pyDes.triple_des(key, pyDes.ECB, IV=None, pad=None, padmode=pyDes.PAD_NORMAL)
    data = base64.decodestring(data)
    d = k.decrypt(data)
    return d


#IV has to be 8bit long
iv = '2132435465768797'
#Key has to be 24bit long
key = binascii.b2a_hex('hSbw2SwTFasdSdddnyS3sijv'.encode())


#here is the data you want to encrypt
data = "dddddddddddddddddddddddddddddddd"

if __name__ == '__main__':
    # print(b'hSbw2SwTFasdSdddnyS3sijvarq')
    # print('hSbw2SwTFasdSdddnyS3sijvarq'.encode())
    # print(binascii.b2a_hex(u'hSbw2SwTFasdSdddnyS3sijv'.encode("utf8")))
    print ("Plan Text: %s" % data)
    encryptdata = encrypt( key, data)
    print ("Encrypted Text: %s" % encryptdata)
    decryptdata = decrypt( key, encryptdata)
    print ("Plan Text: %s" % decryptdata)

