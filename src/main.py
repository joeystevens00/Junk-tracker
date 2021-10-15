# coding=utf-8

from flask import abort, Flask, jsonify, request, render_template
from flask_cors import CORS

from database import Database
from vehicle_registration_service import register_vehicle
from models import vehicle

app = Flask(__name__)
CORS(app) # Please do not do this in production :)

database = Database()

@app.route('/vehicles')
def get_vehicles():
  # TODO
  return jsonify({})

@app.route('/vehicles', methods=['POST'])
def create_vehicle():
  new_vehicle = request.get_json()
  # Look up the model class and creatae a new instance of the model to validate the schema of the request
  validated = vehicle.VEHCILE_TYPE_MAP.get(new_vehicle.get('type'))(new_vehicle)
  dbo = database.create(dict(validated))
  registration_id = register_vehicle(dbo)
  database.update(dbo['id'], {'registration_id': registration_id})
  return jsonify(dbo)

@app.route('/vehicles/<id>')
def get_vehicle(id):
  # TODO
  try:
      dbo = database.find(id)
      return jsonify()
  except:
      abort(404)


@app.route('/vehicles/<id>', methods=['PATCH'])
def update_vehicle(id):
  # TODO
  attrs = request.get_json()
  dbo = database.update(id, attrs)
  return jsonify(dbo)

@app.route('/vehicles/<id>', methods=['DELETE'])
def delete_vehicle(id):
  return jsonify({'deleted': database.destroy(id) or 0})

@app.route('/')
def index():
    return render_template('index.html')
