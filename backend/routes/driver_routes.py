# driver_routes.py

from flask import jsonify, request,make_response
from users.driver import Driver

def driver_profile():
    if request.method == 'POST':
        data = request.json
        driver_id = data['ID']
        driver = Driver(
            id=driver_id,
            name=data['Name'],
            vehicle_num=data['Vehicle_Number'],
            vehicle_type=data['Vehicle_Type'],
            curr_loc=data['Current_Location'],
            is_active=data['Is_Active']
        )
        
        driver.save_to_db()
        return jsonify({"message": "Driver profile set successfully"}), 201
    elif request.method == 'GET':
        driver_id = request.args.get('id')
        driver = Driver.fetch_from_db(driver_id)
        if driver:
            response = make_response(jsonify(driver),200)
            response.headers.set("content-type","application/json")
            return response
        else:
            return jsonify({"message": "Driver not found"}), 404

def action_on_request():
    data = request.json
    driver_id = data['driver_id']
    is_accept = data['is_accept']

    # driver = drivers.get(driver_id)
    if driver:
        action_response, _ = driver.action_on_request(is_accept, data['request_data'])
        return jsonify({"message": action_response}), 200
    else:
        return jsonify({"message": "Driver not found"}), 404
