# patient_routes.py

from flask import jsonify, request,make_response
from users.patient import Patient
from users.driver import Driver
from users.hospital import Hospital

hospitals = {}

def patient_profile():
    if request.method == 'POST':
        data = request.json
        patient = Patient(
            id=data['ID'],
            name=data['Name'],
            age=data['Age'],
            gender=data['Age'],
            curr_loc=data['Current_Location'],
            phone=data['Phone_Number'],
            email=data['Email']
        )
        patient.save_to_db()
        return jsonify({"message": "Patient profile set successfully"}), 201
    
    elif request.method == 'GET':
        patient_id = request.args.get('id')
        patient = Patient.fetch_from_db(patient_id)
        if patient:
            response = make_response(jsonify(patient),200)
            response.headers.set("content-type","application/json")
            return response
        else:
            return jsonify({"message": "Driver not found"}), 404


def book_ambulance():
    data = request.json
    patient_id = data['patient_id']
    hospital_id = data['hospital_id']
    is_emergency = data['is_emergency']

    patient = Patient.fetch_from_db(patient_id)
    hospital = Hospital.fetch_from_db(hospital_id)

    if not (patient and hospital):
        return jsonify({"message": "Patient or hospital not found"}), 404

    active_drivers = Driver.fetch_active_drivers(patient.curr_loc)

    if not active_drivers:
        return jsonify({"message": "No active drivers available"}), 404

    request_data = {
        "patient_id": patient_id,
        "hospital_id": hospital_id,
        "is_emergency": is_emergency,
        "status": "pending"
    }

    response = supabase.table('requests').insert(request_data).execute()

    if response.status_code == 201:
        for driver in active_drivers:
            pass
            # socketio.emit('new_request', driver.get_request(patient, hospital, is_emergency), room=driver.id)
        return jsonify({"message": "Request created and drivers notified"}), 201
    else:
        return jsonify({"message": "Failed to create request"}), 500