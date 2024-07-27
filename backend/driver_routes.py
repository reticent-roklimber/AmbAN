# driver_routes.py

from flask import jsonify, request
from driver import Driver

drivers = {}

def driver_profile():
    if request.method == 'POST':
        data = request.json
        driver_id = data['id']
        driver = Driver(
        id=1,
        name="John Doe",
        vehicle_num="ABC1234",
        vehicle_type="Sedan",
        curr_loc="Downtown",
        is_active=True
    )
        drivers[driver_id] = driver
        driver.save_to_db()  # Save to Supabase
        return jsonify({"message": "Driver profile set successfully"}), 201
    elif request.method == 'GET':
        driver_id = request.args.get('id')
        if not driver_id:
            return jsonify({"error": "ID parameter is required"}), 400
        
        driver = Driver.fetch_from_db(driver_id) 
        print(driver) # Fetch from Supabase
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
        action_response = driver.action_on_request(is_accept)
        return jsonify({"message": action_response}), 200
    else:
        return jsonify({"message": "Driver not found"}), 404


