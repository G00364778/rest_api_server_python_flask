import mysql.connector
import config as cfg
class BookDAO:
    db=""
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database']
        )
    def __init__(self):
        self.connectToDB()

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    def insertIntoSense(self, values):
        cursor = self.getCursor()
        sql="insert into pisense (dts, tempexternal, temponboard, brightness, humidity, barotemp, baropressure, motiondetected) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,values)
        self.db.commit()
        lastRowId=cursor.lastrowid
        cursor.close
        return lastRowId

    def create(self, values):
        cursor = self.getCursor()
        sql="insert into book (title,author, price) values (%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        lastRowId=cursor.lastrowid
        cursor.close
        return lastRowId

    def piGetAll(self):
        cursor = self.getCursor()
        # sql='select idx, dts, tempexternal, temponboard, brightness, humidity, barotemp, baropressure, motiondetected from pisense'
        sql='select idx, dts, tempexternal, temponboard, brightness, humidity, barotemp, baropressure from pisense'
        #colnames = ['idx', 'dts', 'temp', 'temp_pcb', 'lux', 'humid', 'temp_bar' 'press', 'motion']
        colnames = ['idx', 'dts', 'temp', 'temp_pcb', 'lux', 'humid', 'temp_bar' 'press']
        cursor.execute(sql)
        results = cursor.fetchall()
        #print('QueryData: {}'.format(results))
        returnArray = []
        for result in results:
            #print('Result: {}'.format(result))
            returnArray.append(self.convertToDictionary(result,colnames))
        cursor.close
        return returnArray


    def piGetSome(self):
        cursor = self.getCursor()
        sql='select idx, tempexternal, humidity, baropressure from pisense limit 240'
        colnames = ['idx', 'temp', 'humid', 'press']
        cursor.execute(sql)
        results = cursor.fetchall()
        #print('QueryData: {}'.format(results))
        returnArray = []
        for result in results:
            #print('Result: {}'.format(result))
            returnArray.append(self.convertToDictionary(result,colnames))
        cursor.close
        return returnArray


    def getAll(self):
        cursor = self.getCursor()
        sql="select * from book"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        cursor.close
        return returnArray

    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from book where idx = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        book = self.convertToDictionary(result)
        cursor.close()
        return book

    def update(self, values):
        cursor = self.getCursor()
        sql="update book set title= %s,author=%s, price=%s  where idx = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from book where idx = %s"
        values = (id,)

        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")
        cursor.close()

    def convertToDictionary(self, result, colnames=['idx','Title','Author', 'Price']):
        #colnames=['idx','Title','Author', 'Price']
        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        #print("convertToDictionary: ",item)
        return item

bookDAO = BookDAO()