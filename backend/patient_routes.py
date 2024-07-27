# patient_routes.py

from flask import jsonify, request
from patient import Patient

patients = {}

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
    patient.save_to_db()  # Save to Supabase
    return jsonify({"message": "Patient profile set successfully"}), 201
