# patient.py

from supabase import create_client, Client

# Initialize the Supabase client
from config import get_supabase_client


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
        supabase = get_supabase_client()
        response = supabase.table('patients').upsert(data).execute()
        return response

class Hospital:
    def __init__(self, id, name, location, phn_num):
        self.id = id
        self.name = name
        self.location = location
        self.phn_num = phn_num

    def get_details(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Location": self.location,
            "Phone Number": self.phn_num
        }

    def save_to_db(self):
        data = self.get_details()
        supabase = get_supabase_client()
        response = supabase.table('hospitals').upsert(data).execute()
        return response
