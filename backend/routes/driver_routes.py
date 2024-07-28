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
    print("data of action on request::::")
    print(data)
    request_id = data['request_id']
    is_accept = data['is_accept']

    request_response = supabase.table('requests').select('*').eq('ID', request_id).execute()
    request_data = request_response.data[0]
    # driver = drivers.get(driver_id)
  
    if is_accept:
        request_data['status'] = 'accepted'
        trip_data = {
            "request_id": request_id,
            "driver_id": data['driver_id'],
            "patient_id": request_data['patient_id'],
            "hospital_id": request_data['hospital_id'],
            "start_time": data['start_time'],
            "end_time": None
        }
        supabase.table('trips').insert(trip_data).execute()
        # return "Request accepted and trip started", response
    else:
        request_data['status'] = 'rejected'
    
    response = supabase.table('requests').upsert(request_data).execute()

    return jsonify({"message": response.data}), 200
    
