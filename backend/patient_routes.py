# patient_routes.py

from flask import jsonify, request
from patient import Patient
from driver import Driver
from hospital import Hospital

patients = {}
hospitals = {}

def patient_profile():
    patient_id = request.args.get('id')
    patient = patients.get(patient_id)
    if patient:
        return jsonify(patient.get_profile()), 200
    else:
        return jsonify({"message": "Patient not found"}), 404

def create_patient_profile():
    data = request.json
    patient_id = data['id']
    patient = Patient(
        id=patient_id,
        name=data['name'],
        age=data['age'],
        gender=data['gender'],
        curr_loc=data['curr_loc']
    )
    patients[patient_id] = patient
    patient.save_to_db()
    return jsonify({"message": "Patient profile set successfully"}), 201

def create_hospital_profile():
    data = request.json
    hospital_id = data['id']
    hospital = Hospital(
        id=hospital_id,
        name=data['name'],
        location=data['location'],
        phn_num=data['phn_num']
    )
    hospitals[hospital_id] = hospital
    hospital.save_to_db()
    return jsonify({"message": "Hospital profile set successfully"}), 201

def hospital_details():
    hospital_id = request.args.get('id')
    hospital = hospitals.get(hospital_id)
    if hospital:
        return jsonify(hospital.get_details()), 200
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
