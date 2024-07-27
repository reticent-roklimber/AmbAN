# app.py

from flask import Flask, request
from driver_routes import driver_profile, action_on_request
from patient_routes import patient_profile
from hospital_routes import hospital_details, book_ambulance
from driver import Driver
from patient import Patient, Hospital

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def test():
    return "HELLO"

@app.route('/driver/profile', methods=['GET'])
def handle_driver_profile():
    # args= request.args
    # id= args.get('id')
    print("Inside get call")
    return "driver_profile(id)"

@app.route('/patient/profile', methods=['GET'])
def handle_patient_profile():
    return patient_profile()

@app.route('/hospital/details', methods=['GET'])
def handle_hospital_details():
    return hospital_details()

@app.route('/book_ambulance', methods=['POST'])
def handle_book_ambulance():
    return book_ambulance()

@app.route('/action_on_request', methods=['POST'])
def handle_action_on_request():
    return action_on_request()


if __name__ == '__main__':
    # Creating some initial data for demonstration
    from driver_routes import drivers
    from patient_routes import patients
    from hospital_routes import hospitals
    from config import get_supabase_client

    supabase = get_supabase_client()
    print(supabase)
    app.run(debug=True)
