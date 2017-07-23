import sqlite3
import pymssql

class DB:
    def connectToDB(self,dbName):
        self.__DB = sqlite3.connect(str(dbName))
    def DBinsert(self,tableName,infoDict):
        sentence = "insert into " + str(tableName) + " ("
        for key in infoDict.keys():
            sentence += str(key) + " ,"
        sentence = sentence[:-1]
        sentence += ") values ("
        for value in infoDict.values():
            if type(value) == str:
                sentence += "'" + value + "'" + " ,"
            else:
                sentence += str(value) + " ,"
        sentence = sentence[:-1]
        sentence += ");"
        try:
            result = self.__DB.execute(sentence)
        except:
            return False
        self.__DB.commit()
        return True
    def DBsearch(self,tableName,columnTuble,limitationDict=None):#要特别注意传进来的tuble如果只有一个变量名时的时候需要加个逗号（X,)
        sentence = "select "
        if columnTuble:
            for columnName in columnTuble:
                sentence += str(columnName) + " ,"
            sentence = sentence[:-1]
            sentence += "from " + str(tableName) + " "
        else:
            sentence += " * from " + str(tableName) + " "
        if limitationDict:
            sentence += "where "
            for key in limitationDict:
                if type(limitationDict[key]) == str:
                    sentence += str(key) + "=" + "'" + limitationDict[key] + "'"
                else:
                    sentence += str(key) + "=" + str(limitationDict[key])
                sentence += " and "
            sentence = sentence[:-4]
        sentence += ";"
        result = self.__DB.execute(sentence)
        self.__DB.commit()
        resultToDict = {}
        i = 0
        for row in result:
            resultToDict[i] = row
            i += 1
        return resultToDict
    def DBdelete(self,tableName,limitationDict=None):
        sentence = "delete from " + str(tableName) + " "
        if limitationDict:
            sentence += "where "
            for key in limitationDict:
                if type(limitationDict[key]) == str:
                    sentence += str(key) + "=" + "'" + limitationDict[key] + "'"
                else:
                    sentence += str(key) + "=" + str(limitationDict[key])
                sentence += " and "
            sentence = sentence[:-4]
            sentence += ";"
        try:
            result = self.__DB.execute(sentence)
        except:
            return False
        self.__DB.commit()
        return result
    def DBupdate(self, tableName, newInfoDict, limitationDict=None):
        if newInfoDict:
            sentence = "update " + str(tableName) + " "
            sentence += "set "
            for key in newInfoDict:
                if type(newInfoDict[key]) == str:
                    sentence += str(key) + "=" + "'" + newInfoDict[key] + "'" + " ,"
                else:
                    sentence += str(key) + "=" + str(newInfoDict[key]) + " ,"
            sentence = sentence[:-1]
            if limitationDict:
                sentence += "where "
                for key in limitationDict:
                    if type(limitationDict[key]) == str:
                        sentence += str(key) + "=" + "'" + limitationDict[key] + "'"
                    else:
                        sentence += str(key) + "=" + str(limitationDict[key])
                    sentence += " and "
                sentence = sentence[:-4]#去除多余的and
                sentence += ";"
            else:
                return False
            try:
                self.__DB.execute(sentence)
                self.__DB.commit()
                return True
            except:
                return  False
        else:
            return False

if __name__ == '__main__':
    db = DB()
    db.connectToDB(dbName="DBname.db")#连接数据库
    db.DBinsert(tableName="table1",infoDict={'name':'lzn','age':22})#所有的操作都是commit的
    db.DBupdate(tableName='table1',newInfoDict={'name':'Liangzn'},limitationDict={"age":22})
    db.DBsearch(tableName='table1',columnTuble=('name',),limitationDict={})#没有limitation的时候传空字典,列名元组只有一个元素的时候需要加个逗号
    db.DBdelete(tableName='table1',limitationDict={'name':"Liangzn"})#所有的操作都是成功的时候返回True,否则Flase