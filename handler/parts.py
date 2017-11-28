from flask import jsonify
from dao.parts import PartsDAO


class PartHandler:
    def build_part_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pname'] = row[1]
        result['pmaterial'] = row[2]
        result['pcolor'] = row[3]
        result['pprice'] = row[4]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['scity'] = row[2]
        result['sphone'] = row[3]
        return result

    def getAllParts(self):
        dao = PartsDAO()
        parts_list = dao.getAllParts()
        result_list = []
        for row in parts_list:
            result = self.build_part_dict(row)
            result_list.append(result)
        return jsonify(Parts=result_list)

    def getPartById(self, pid):
        dao = PartsDAO()
        row = dao.getPartById(pid)
        if not row:
            return jsonify(Error = "Part Not Found"), 404
        else:
            part = self.build_part_dict(row)
            return jsonify(Part = part)

    def searchParts(self, args):
        color = args.get("color")
        material = args.get("material")
        dao = PartsDAO()
        parts_list = []
        if color and material:
            parts_list = dao.getPartsByColorAndMaterial(color, material)
        elif color:
            parts_list = dao.getPartsByColor(color)
        elif material:
            parts_list = dao.getPartsByMaterial(material)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in parts_list:
            result = self.build_part_dict(row)
            result_list.append(result)
        return jsonify(Parts=result_list)

    def getSuppliersByPartId(self, pid):
        dao = PartsDAO()
        suppliers_list = dao.getSuppliersByPartId(pid)
        if not suppliers_list:
            return jsonify(Error="Part Not Found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplier_dict(row)
                result_list.append(result)
            return jsonify(Suppliers=result_list)