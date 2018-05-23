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

    def build_part_attributes(self, pid, pname, pcolor, pmaterial, pprice):
        result = {}
        result['pid'] = pid
        result['pname'] = pname
        result['pmaterial'] = pcolor
        result['pcolor'] = pmaterial
        result['pprice'] = pprice
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
        if (len(args) == 2) and color and material:
            parts_list = dao.getPartsByColorAndMaterial(color, material)
        elif (len(args) == 1) and color:
            parts_list = dao.getPartsByColor(color)
        elif (len(args) == 1) and material:
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
        if not dao.getPartById(pid):
            return jsonify(Error="Part Not Found"), 404
        suppliers_list = dao.getSuppliersByPartId(pid)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def insertPart(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            pname = form['pname']
            pprice = form['pprice']
            pmaterial = form['pmaterial']
            pcolor = form['pcolor']
            if pcolor and pprice and pmaterial and pname:
                dao = PartsDAO()
                pid = dao.insert(pname, pcolor, pmaterial, pprice)
                result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertPartJson(self, json):
        pname = json['pname']
        pprice = json['pprice']
        pmaterial = json['pmaterial']
        pcolor = json['pcolor']
        if pcolor and pprice and pmaterial and pname:
            dao = PartsDAO()
            pid = dao.insert(pname, pcolor, pmaterial, pprice)
            result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
            return jsonify(Part=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deletePart(self, pid):
        dao = PartsDAO()
        if not dao.getPartById(pid):
            return jsonify(Error = "Part not found."), 404
        else:
            dao.delete(pid)
            return jsonify(DeleteStatus = "OK"), 200

    def updatePart(self, pid, form):
        dao = PartsDAO()
        if not dao.getPartById(pid):
            return jsonify(Error = "Part not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                pname = form['pname']
                pprice = form['pprice']
                pmaterial = form['pmaterial']
                pcolor = form['pcolor']
                if pcolor and pprice and pmaterial and pname:
                    dao.update(pid, pname, pcolor, pmaterial, pprice)
                    result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
                    return jsonify(Part=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def build_part_counts(self, part_counts):
        result = []
        #print(part_counts)
        for P in part_counts:
            D = {}
            D['id'] = P[0]
            D['name'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result

    def getCountByPartId(self):
        dao = PartsDAO()
        result = dao.getCountByPartId()
        #print(self.build_part_counts(result))
        return jsonify(PartCounts = self.build_part_counts(result)), 200



