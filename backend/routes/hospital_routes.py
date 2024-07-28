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
        
def fetch_nearby_hospitals():
    patient_location = request.args.get('location')  # Coordinates in string format "lat,lon"
    patient_coords = tuple(map(float, patient_location.split(',')))

    response = supabase.table('hospitals').select('*').execute()
    hospitals_data = response.data

    hospitals = []
    for data in hospitals_data:
        hospital_coords = tuple(map(float, data['Location'].split(',')))
        distance = geodesic(patient_coords, hospital_coords).km
        hospitals.append((distance, data))

    hospitals.sort(key=lambda x: x[0])
    nearby_hospitals = [hospital for distance, hospital in hospitals[:5]]
    return jsonify(nearby_hospitals)