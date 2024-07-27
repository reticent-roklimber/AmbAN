# app.py

from flask import Flask,make_response
from driver_routes import driver_profile, action_on_request
from patient_routes import patient_profile, create_patient_profile, book_ambulance
from hospital_routes import hospital_details, create_hospital_profile



app = Flask(__name__)

@app.route('/driver/profile', methods=['GET', 'POST'])
def handle_driver_profile():
    print("handle_driver called")
    return driver_profile()

@app.route('/patient/profile', methods=['GET'])
def handle_patient_profile():
    return patient_profile()

@app.route('/patient/create_profile', methods=['POST'])
def handle_create_patient_profile():
    return create_patient_profile()

@app.route('/hospital/details', methods=['GET'])
def handle_hospital_details():
    return hospital_details()

@app.route('/hospital/create_profile', methods=['POST'])
def handle_create_hospital_profile():
    return create_hospital_profile()

@app.route('/book_ambulance', methods=['POST'])
def handle_book_ambulance():
    return book_ambulance()

@app.route('/action_on_request', methods=['POST'])
def handle_action_on_request():
    return action_on_request()

if __name__ == '__main__':

    from config import get_supabase_client

    supabase = get_supabase_client()

    app.run(debug=True)
