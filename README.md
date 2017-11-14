# 短信服务python 版本使用说明 #

## 版本变更记录 ##

- 1.0.0 : 初稿


## 目录 ##

[1. 概述](#1)

&nbsp;&nbsp;&nbsp;&nbsp;[1.1 简介](#1.1)

&nbsp;&nbsp;&nbsp;&nbsp;[1.2 如何获取](#1.2)

[2. API](#2)

&nbsp;&nbsp;&nbsp;&nbsp;[2.1 短信发送](#2.1)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[行业短信发送](#2.1.1)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[营销短信发送](#2.1.2)

&nbsp;&nbsp;&nbsp;&nbsp;[2.2 接受通知(状态报告)](#2.2)

&nbsp;&nbsp;&nbsp;&nbsp;[2.3 查询短信发送结果(状态报告)](#2.3)


[3. DEMO](#3)

<h2 id='1'> 1. 概述 </h2>

<h4 id='1.1'> 1.1 简介 </h4>

-  短信服务SDK python版本,请使用python3 及以上版本。

<h4 id='1.2'> 1.2 如何获取 </h4>

[获取源码](https://github.com/ipaynowORG/ipaynow_sms_python.git)



<h2 id='2'> 2. API </h2>

业务服务端使用的相关模块: message.py

<h4 id='2.1'> 2.1 短信发送 </h4>

<h5 id='2.1.1'></h4>

- 行业短信发送

        '''
         行业短信
         appId 商户应用Id 
         appKey 商户应用秘钥
         desKey des秘钥
         mhtOrderNo 商户订单号
         mobile 发送手机号 
         content 短信内容
         notifyUrl 后台通知地址
        '''
        def industryMessage(appId, appKey,desKey, mhtOrderNo, mobile,content, notifyUrl)             

<h5 id='2.1.2'></h4>

- 营销短信发送

        '''
         营销短信
         appId 商户应用Id 
         appKey 商户应用秘钥
         desKey des秘钥
         mhtOrderNo 商户订单号
         mobile 发送手机号 
         content 短信内容 （内容请加 回复TD退订）
         notifyUrl 后台通知地址
        '''
        def salesMessage(appId, appKey,desKey, mhtOrderNo, mobile,content, notifyUrl)


<h4 id='2.2'>2.2 接受通知(状态报告)</h4>

由现在支付方发起,POST请求


字段含义如下:

<table>
        <tr>
            <th>字段名称</th>
            <th>字段Key</th>
            <th>备注</th>
        </tr>
        <tr>
            <td>功能码</td>
            <td>funcode</td>
            <td>同下行时候的输入,S01或YX_01</td>
        </tr>
        <tr>
            <td>商户应用ID</td>
            <td>appId</td>
            <td>同输入</td>
         </tr>
<tr>
            <td>手机号</td>
            <td>phone</td>
            <td>下行手机号</td>
         </tr>
<tr>
            <td>商户订单号</td>
            <td>mhtOrderNo</td>
            <td>同输入</td>
         </tr>
<tr>
            <td>订单生成时间</td>
            <td>mhtOrderStartTime</td>
            <td></td>
         </tr>
<tr>
            <td>现在支付订单号</td>
            <td>nowPayOrderNo</td>
            <td></td>
         </tr>
<tr>
            <td>字符编码</td>
            <td>mhtCharset</td>
            <td>定值UTF-8</td>
         </tr>
<tr>
            <td>签名类型</td>
            <td>signType</td>
            <td>定值MD5</td>
         </tr>
<tr>
            <td>签名值</td>
            <td>signature</td>
            <td></td>
         </tr>
<tr>
            <td>推送状态</td>
            <td>tradeStatus</td>
            <td>A001:成功。A002:失败。 A00H:处理中</td>
         </tr>
    </table>

<h4 id='2.3'> 2.3 查询短信发送结果(状态报告) </h4>

- 查询短信发送结果(状态报告)

        ''' 
         短信查询   
         appId 商户应用Id 
         appKey 商户应用秘钥
         nowPayOrderNo 现在支付订单号
         mobile 手机号   
        '''
        def query(appId, appKey, nowPayOrderNo, mobile)              

<h2 id='3'> 3. DEMO </h2>
   messageTest.py
