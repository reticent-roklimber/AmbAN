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
    driver_id = data['driver_id']

    patient = Patient.fetch_from_db(patient_id)
    hospital = Hospital.fetch_from_db(hospital_id)
    driver = Driver.fetch_from_db(driver_id)

    if patient and hospital and driver and driver.is_active:
        request_data = driver.get_request(patient, hospital, is_emergency)
        return jsonify({"request_data": request_data}), 200
    else:
        return jsonify({"message": "Active driver or patient or hospital not found"}), 404
