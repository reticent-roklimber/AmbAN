# patient.py

from config import get_supabase_client

supabase = get_supabase_client()

class Patient:
    def __init__(self, id, name, age, gender, curr_loc):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.curr_loc = curr_loc

    def get_profile(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Current Location": self.curr_loc
        }

    def save_to_db(self):
        data = self.get_profile()
        response = supabase.table('patients').upsert(data).execute()
        return response

    @classmethod
    def fetch_from_db(cls, patient_id):
        response = supabase.table('patients').select('*').eq('ID', patient_id).execute()
        data = response.data[0]
        return cls(
            id=data['ID'],
            name=data['Name'],
            age=data['Age'],
            gender=data['Gender'],
            curr_loc=data['Current Location']
        )
