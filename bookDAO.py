import mysql.connector
import config as cfg
class BookDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
        )        
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into book (title,author, price) values (%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        #print("Cursor: ",cursor)
        #print("Rowid: ",cursor.lastrowid)
        return cursor.lastrowid
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from book"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        return returnArray
    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from book where idx = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)
    def update(self, values):
        cursor = self.db.cursor()
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
    def convertToDictionary(self, result):
        colnames=['idx','Title','Author', "Price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        #print("convertToDictionary: ",item)
        return item
        
bookDAO = BookDAO()