from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# VM Type Class/Model
class Vm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instance_type = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, instance_type, price):
        self.instance_type = instance_type
        self.price = price

# VM Type Schema
class VmSchema(ma.Schema):
    class Meta:
        fields = ('id', 'instance_type', 'price')

# Init schema
vm_schema = VmSchema()
vms_schema = VmSchema(many=True)

# Create a vm type
@app.route('/vm', methods=['POST'])
def add_vm():
    instance_type = request.json['instance_type']
    price = request.json['price']

    new_vm = Vm(instance_type, price)
    db.session.add(new_vm)
    db.session.commit()

    return vm_schema.jsonify(new_vm)

# Update vm
@app.route('/vm/<id>', methods=['PUT'])
def update_vm(id):
    get_vm = Vm.query.get(id)
    
    instance_type = request.json['instance_type']
    price = request.json['price']

    get_vm.instance_type = instance_type
    get_vm.price = price

    db.session.commit()

    return vm_schema.jsonify(get_vm)

# Get all vms
@app.route('/vm', methods=["GET"])
def get_vms():
    all_vm = Vm.query.all()
    results = vms_schema.dump(all_vm)
    return jsonify(results)

# Get single vm
@app.route('/vm/<id>', methods=["GET"])
def get_vm(id):
    get_vm = Vm.query.get(id)
    return vm_schema.jsonify(get_vm)

# Delete single vm
@app.route('/vm/<id>', methods=["DELETE"])
def delete_vm(id):
    delete_vm = Vm.query.get(id)
    db.session.delete(delete_vm)
    db.session.commit()

    return vm_schema.jsonify(delete_vm)

@app.route('/vm/type/<instance_type>', methods=['GET'])
def get_specific_vm(instance_type):
    filter_vm = Vm.query.filter(Vm.instance_type == instance_type)
    result = vms_schema.dump(filter_vm)
    return jsonify(result)

# Run server
if __name__ == "__main__":
    app.run(debug=True)