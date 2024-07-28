# patient.py

from config import get_supabase_client

supabase = get_supabase_client()

class Patient:
    def __init__(self, id, name, age, gender, curr_loc,email,phone):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.curr_loc = curr_loc
        self.email = email
        self.phone = phone

    def get_profile(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Current_Location": self.curr_loc,
            "Email":self.email,
            "Phone_Number":self.phone
        }

    def save_to_db(self):
        data = self.get_profile()
        try:
            response = supabase.table('patients').upsert(data).execute()
        except Exception:
            return {"error": "Could not save data" , "code":404}
        return response

    @classmethod
    def fetch_from_db(cls, patient_id):
        response = supabase.table('patients').select('*').eq('ID', patient_id).execute()
        try:
            data = response.data[0]
        except IndexError:
            return {"error":"No data in database","code":404}
        return data

