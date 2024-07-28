# hospital_routes.py

from flask import jsonify, request
from users.hospital import Hospital

hospitals = {}

def hospital_details():
    if request.method == 'POST':
        data = request.json
        hospital = Hospital(
            id=data['ID'],
            name=data['Name'],
            location=data['Location'],
            phn_num=data['Phone_Number']
        )
        hospital.save_to_db()
        return jsonify({"message": "Hospital profile set successfully"}), 201
    elif request.method == 'GET':
        hospital_id = request.args.get('id')
        hospital_data = Hospital.fetch_from_db(hospital_id)
        if hospital_data:
            print(hospital_data)
            return jsonify(hospital_data), 200
        else:
            return jsonify({"message": "Hospital not found"}), 404
        
def book_ambulance():
    data = request.json
    patient_id = data['patient_id']
    hospital_id = data['hospital_id']
    is_emergency = data['is_emergency']
    driver_id = data['driver_id']

    patient = Patient.fetch_from_db(patient_id)
    hospital = Hospital.fetch_from_db(hospital_id)
    driver = Driver.fetch_from_db(driver_id)

    if patient and hospital and driver and driver.is_active:
        request_data = driver.get_request(patient, hospital, is_emergency)
        return jsonify({"request_data": request_data}), 200
    else:
        return jsonify({"message": "Active driver or patient or hospital not found"}), 404
