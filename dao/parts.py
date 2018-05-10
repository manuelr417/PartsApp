from config.dbconfig import pg_config
import psycopg2
class PartsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllParts(self):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPartById(self, pid):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def getPartsByColor(self, color):
        cursor = self.conn.cursor()
        query = "select * from parts where pcolor = %s;"
        cursor.execute(query, (color,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPartsByMaterial(self, material):
        cursor = self.conn.cursor()
        query = "select * from parts where pmaterial = %s;"
        cursor.execute(query, (material,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPartsByColorAndMaterial(self, color, material):
        cursor = self.conn.cursor()
        query = "select * from parts where pmaterial = %s and pcolor = %s;"
        cursor.execute(query, (material,color))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByPartId(self, pid):
        cursor = self.conn.cursor()
        query = "select sid, sname, scity, sphone from parts natural inner join supplier natural inner join supplies where pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        cursor = self.conn.cursor()
        query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def delete(self, pid):
        cursor = self.conn.cursor()
        query = "delete from parts where pid = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        cursor = self.conn.cursor()
        query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        self.conn.commit()
        return pid

    def getCountByPartId(self):
        cursor = self.conn.cursor()
        query = "select pid, pname, sum(stock) from parts natural inner join supplies group by pid, pname order by pname;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


