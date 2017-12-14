from flask import Flask, jsonify, request
from handler.parts import PartHandler
from handler.supplier import SupplierHandler



app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'

@app.route('/PartApp/parts', methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'POST':
        return PartHandler().insertPart(request.form)
    else:
        if not request.args:
            return PartHandler().getAllParts()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/PartApp/parts/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
def getPartById(pid):
    if request.method == 'GET':
        return PartHandler().getPartById(pid)
    elif request.method == 'PUT':
        return PartHandler().updatePart(pid, request.form)
    elif request.method == 'DELETE':
        return PartHandler().deletePart(pid)
    else:
        return jsonify(Error="Method not allowerd."), 405

@app.route('/PartApp/parts/<int:pid>/suppliers')
def getSuppliersByPartId(pid):
    return PartHandler().getSuppliersByPartId(pid)

@app.route('/PartApp/suppliers')
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return SupplierHandler().searchSuppliers(request.args)

@app.route('/PartApp/suppliers/<int:sid>')
def getSupplierById(sid):
    return SupplierHandler().getSupplierById(sid)

@app.route('/PartApp/suppliers/<int:sid>/parts')
def getPartsBySuplierId(sid):
    return SupplierHandler().getPartsBySupplierId(sid)

if __name__ == '__main__':
    app.run()