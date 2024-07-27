# hospital_routes.py

from flask import jsonify, request
from patient import Hospital

hospitals = {}

def hospital_details():
    hospital_id = request.args.get('id')
    hospital = hospitals.get(hospital_id)
    if hospital:
        return jsonify(hospital.get_details()), 200
    else:
        return jsonify({"message": "Hospital not found"}), 404

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
    hospital.save_to_db()  # Save to Supabase
    return jsonify({"message": "Hospital profile set successfully"}), 201

def book_ambulance():
    data = request.json
    patient_id = data['patient_id']
    hospital_id = data['hospital_id']
    is_emergency = data['is_emergency']

    from driver_routes import drivers
    from patient_routes import patients

    patient = patients.get(patient_id)
    hospital = hospitals.get(hospital_id)

    if not patient or not hospital:
        return jsonify({"message": "Patient or Hospital not found"}), 404

    driver_id = data['driver_id']
    driver = drivers.get(driver_id)

    if driver and driver.is_active:
        request_details = driver.get_request(patient, hospital, is_emergency)
        return jsonify(request_details), 200
    else:
        return jsonify({"message": "Active driver not found"}), 404
