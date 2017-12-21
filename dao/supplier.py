from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, sid):
            cursor = self.conn.cursor()
            query = "select * from supplier where sid = %s;"
            cursor.execute(query, (sid,))
            result = cursor.fetchone()
            return result

    def getPartsBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice, qty from parts natural inner join supplier natural inner join supplies where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByCity(self, city):
        cursor = self.conn.cursor()
        query = "select * from supplier where scity = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, sname, scity, sphone):
        cursor = self.conn.cursor()
        query = "insert into supplier(sname, scity, sphone) values (%s, %s, %s) returning sid;"
        cursor.execute(query, (sname, scity, sphone))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid