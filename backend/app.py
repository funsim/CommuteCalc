#!flask/bin/python
from flask import Flask, jsonify, request
from datetime import time

app = Flask(__name__)

@app.route('/commutecalc/api')
def index():
    return "Welcome to the CommuteCalc API!"

pickups = [
    {
        'id': 1,
        'name': u'Place 1',
        'lat': 30,
        'lon': 30
    },
    {
        'id': 2,
        'name': u'Place 2',
        'lat': 34,
        'lon': 10
    }
]

drivers = [
    {
        'id': 1,
        'name': u'Simon Funke',
        'contact': u'00000',
        'pickup_id': 2, 
        'time': str(time(hour=8, minute=30))
    },
    {
        'id': 2,
        'name': u'Franz Viertel',
        'contact': u'00000',
        'pickup_id': 1, 
        'time': str(time(hour=9, minute=30))
    }
]


@app.route('/commutecalc/api/pickups', methods = ['GET'])
def get_pickups():
    return jsonify( { 'pickups': pickups } )

@app.route('/commutecalc/api/pickups/<int:pickup_id>', methods = ['GET'])
def get_pickup(pickup_id):
    pickup = filter(lambda t: t['id'] == pickup_id, pickups)
    if len(pickup) == 0:
        abort(404)
    return jsonify( { 'pickup': pickup[0] } )

@app.route('/commutecalc/api/pickups/<int:pickup_id>/drivers', methods = ['GET'])
def get_pickup(pickup_id):
    driver_list = filter(lambda t: t['pickup_id'] == pickup_id, drivers)
    return jsonify( { 'drivers': driver_list } )

@app.route('/commutecalc/api/drivers', methods = ['GET'])
def get_drivers():
    return jsonify( { 'drivers': drivers } )

@app.route('/commutecalc/api/drivers/<int:driver_id>', methods = ['GET'])
def get_driver(driver_id):
    driver = filter(lambda t: t['id'] == driver_id, drivers)
    if len(driver) == 0:
        abort(404)
    return jsonify( { 'driver': driver[0] } )

@app.route('/commutecalc/api/drivers', methods = ['POST'])
def create_driver():
    if not request.json or not 'name' in request.json:
        abort(400)
    driver = {
        'id': drivers[-1]['id'] + 1,
        'name': request.json['name'],
        'pickup_id': request.json.get('pickup_id'),
        'time': request.json.get('time')
    }
    drivers.append(driver)
    return jsonify( { 'driver': driver } ), 201

if __name__ == '__main__':
    app.run(debug = True)
