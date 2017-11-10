#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4
import base64
import urllib

from ipaynow_sms.error import APIInputError
from ipaynow_sms.desUtil import base64Encryt, md5Encrypt, desEncrypt
from ipaynow_sms.paramlist import S01_PostList

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
import getopt, sys


def usage():
    print('''
NAME
    pack send message.
Usage
    python packMsg.py [options]
    ''')


class PackMsgSend:
    __srcDict = {}
    __tarDict = {}
    __tarDictJoinMd5 = {}
    __tarListJoinMd5 = []
    __filterRule = []
    __fromStrMd5 = ""
    __appId = ""
    __md5Key = ""
    __3desKsy = ""
    __md5Result = ""
    __message1 =""
    __message2 = ""
    __message3 = ""


    def __init__(self,appId, appKey,desKey, sourcedict={}, filterrule=[]):
        self.__appId = appId
        self.__md5Key = appKey
        self.__3desKsy = desKey
        self.__srcDict = sourcedict
        self.__filterRule = filterrule

    def __inputFilter(self):
        '''
        from __srcDict to __tarDict
        use paramlist to filter the input dictionary.
        '''
        for singleParam in self.__filterRule:
            filedName = singleParam['name']
            # judeg if the filedName exist in source dictionary.
            if filedName in self.__srcDict:  # exist
                # the filedName is exist in sourcedict.
                # then judge if the length is right.
                srcContent = self.__srcDict[filedName]
                if (len(str(srcContent)) > singleParam['len']):
                    errmsg = '''Your input parameter [{}] is too long. Max length is [{}].'''.format(filedName,
                                                                                                     singleParam['len'])
                    raise APIInputError(errmsg)
                if (len(str(srcContent)) == 0):
                    continue
                self.__tarDict[filedName] = srcContent
                # if the info needs md5 calc .
                if (singleParam['md5'] == 'Y'):
                    self.__tarDictJoinMd5[filedName] = srcContent
            else:  # no exist
                # judge if the parameter is mandatory
                if singleParam['mandatory'] == 'Y':  # this parameter is mandatory
                    if filedName == 'mhtSignature':
                        continue
                    errmsg = '''You should input parameter [{}].this parameter indicts [{}].'''.format(filedName,
                                                                                                       singleParam[
                                                                                                           'desp'])
                    raise APIInputError(errmsg)
                else:
                    continue
        self.__sortDict()

    def __sortDict(self):
        sortedListJoinmd5 = sorted(self.__tarDictJoinMd5.items(), key=lambda e: e[0], reverse=False)
        self.__tarListJoinMd5 = sortedListJoinmd5

    def __createFromStr(self):
        fromstrmd5 = ""
        for formContentMd5 in self.__tarListJoinMd5:
            if formContentMd5[1] == '' or formContentMd5[1] == None:
                continue
            fromstrmd5 += str(formContentMd5[0]) + "=" + str(formContentMd5[1]) + "&"
        self.__fromStrMd5 = fromstrmd5[:-1]

    def getResultString(self):
        self.__inputFilter()
        self.__createFromStr()
        self.__message1 = base64.b64encode(("appId="+self.__appId).encode(encoding="utf-8")).decode() #base64.encodebytes(binascii.b2a_hex(("appId="+self.__appId).encode()))
        print("第一部分：" + self.__message1)
        self.__message2 = desEncrypt(self.__3desKsy,self.__fromStrMd5).decode() #base64(3DES(报文原文)
        print("第二部分：" +self.__message2.replace(" ",""))
        print("md5 明文" + self.__fromStrMd5 + "&" + self.__md5Key)
        print("md5 密文" + md5Encrypt(self.__fromStrMd5 + "&" + self.__md5Key))
        self.__message3 = base64.b64encode(md5Encrypt(self.__fromStrMd5 + "&" + self.__md5Key).encode(encoding="utf-8")).decode()#base64(MD5(报文原文+&+ md5Key))
        print("第三部分：" +self.__message3)
        #self.__calcMd5()
        urlstr = self.__message1 + "|" + self.__message2 + "|" + self.__message3
        resultStr = urllib.parse.quote(urlstr)
        print(resultStr)
        # resultStr = urlencode(urlstr)
        return resultStr

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    file = ""

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--file"):
            file = a
        else:
            assert False, "unhandled option"
    paypara = {
        'funcode': "S01",
        'appId': "150753086263684",
        'mhtOrderNo': "industry2",
        'content':'python测试',
        'mobile': "17701087752",
        'notifyUrl': "www.baidu.com",
    }
    try:
        pms = PackMsgSend("150753086263684","zHGKLmQaU9PLMEGObyubsV5uhDAeYVqQ","w75zriHtT85zpCYW3y8Dpw2k", paypara, S01_PostList)
        resultStr = pms.getResultString()
    except APIInputError as e:
        print(e)

    print("============")
    # print(quote_plus(resultStr,safe='=&'))
