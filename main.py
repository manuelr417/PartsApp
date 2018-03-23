from flask import Flask, jsonify, request
from handler.parts import PartHandler
from handler.supplier import SupplierHandler


# Activate
app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'

@app.route('/PartApp/parts')
def getAllParts():
    if not request.args:
        return PartHandler().getAllParts()
    else:
        return PartHandler().searchParts(request.args)

@app.route('/PartApp/parts/<int:pid>')
def getPartById(pid):
    return PartHandler().getPartById(pid)

@app.route('/PartApp/parts/<int:pid>/suppliers')
def getSuppliersByPartId(pid):
    return PartHandler().getSuppliersByPartId(pid)

@app.route('/PartApp/suppliers')
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return PartHandler().searchParts(request.args)

@app.route('/PartApp/suppliers/<int:sid>')
def getSupplierById(sid):
    return SupplierHandler().getSupplierById(sid)

@app.route('/PartApp/suppliers/<int:sid>/parts')
def getPartsBySuplierId(sid):
    return SupplierHandler().getPartsBySupplierId(sid)

if __name__ == '__main__':
    app.run()