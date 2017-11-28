from flask import jsonify
from dao.supplier import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['scity'] = row[2]
        result['sphone'] = row[3]
        return result

    def build_part_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pname'] = row[1]
        result['pmaterial'] = row[2]
        result['pcolor'] = row[3]
        result['pprice'] = row[4]
        result['quantity'] = row[5]
        return result

    def getAllSuppliers(self):

        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(records=result_list)

    def getSupplierById(self, sid):

        dao = SupplierDAO()

        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            part = self.build_supplier_dict(row)
        return jsonify(Part=part)

    
    def getPartsBySupplierId(self, sid):
        dao = SupplierDAO()
        parts_list = dao.getPartsBySupplierId(sid)
        if not parts_list:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            result_list = []
            for row in parts_list:
                result = self.build_part_dict(row)
                result_list.append(result)
            return jsonify(Parts=result_list)
