# driver_routes.py

from flask import jsonify, request
from driver import Driver

drivers = {}

def driver_profile():
    if request.method == 'POST':
        data = request.json
        driver_id = data['id']
        driver = Driver(
            id=driver_id,
            name=data['name'],
            vehicle_num=data['vehicle_num'],
            vehicle_type=data['vehicle_type'],
            curr_loc=data['curr_loc'],
            is_active=data['is_active']
        )
        drivers[driver_id] = driver
        driver.save_to_db()
        return jsonify({"message": "Driver profile set successfully"}), 201
    elif request.method == 'GET':
        driver_id = request.args.get('id')
        driver = drivers.get(driver_id)
        if driver:
            return jsonify(driver.get_profile()), 200
        else:
            return jsonify({"message": "Driver not found"}), 404

def action_on_request():
    data = request.json
    driver_id = data['driver_id']
    is_accept = data['is_accept']

    driver = drivers.get(driver_id)
    if driver:
        action_response, _ = driver.action_on_request(is_accept, data['request_data'])
        return jsonify({"message": action_response}), 200
    else:
        return jsonify({"message": "Driver not found"}), 404
