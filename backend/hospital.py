# hospital.py

from config import get_supabase_client

supabase = get_supabase_client()

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
            "Phone_Number": self.phn_num
        }

    def save_to_db(self):
        data = self.get_details()
        response = supabase.table('hospitals').upsert(data).execute()
        return response

    @classmethod
    def fetch_from_db(cls, hospital_id):
        response = supabase.table('hospitals').select('*').eq('ID', hospital_id).execute()
        try:
            data = response.data[0]
        except IndexError:
            return {"error":"No data in database","code":404}
        return data