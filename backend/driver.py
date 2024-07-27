from supabase import create_client, Client
from config import get_supabase_client

class Driver:
    def __init__(self, id, name=None, vehicle_num=None, vehicle_type=None, curr_loc=None, is_active=None):
        self.id = id
        self.name = name
        self.vehicle_num = vehicle_num
        self.vehicle_type = vehicle_type
        self.curr_loc = curr_loc
        self.is_active = is_active

    def get_profile(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Vehicle_Number": self.vehicle_num,
            "Vehicle_Type": self.vehicle_type,
            "Current_Location": self.curr_loc,
            "Is_Active": self.is_active
        }

    def set_profile(self, name, vehicle_num, vehicle_type, curr_loc, is_active):
        self.name = name
        self.vehicle_num = vehicle_num
        self.vehicle_type = vehicle_type
        self.curr_loc = curr_loc
        self.is_active = is_active

    def save_to_db(self):
        data = self.get_profile()
        supabase = get_supabase_client()
        response = supabase.table('drivers').upsert(data).execute()
        return response

    def get_profile(driver_id):
        print("Inside get profile...")
        supabase = get_supabase_client()
        response = supabase.table('drivers').select('*').eq('ID', driver_id).execute()
        
        if response.data:
            driver_data = response.data[0]  # Assuming ID is unique, so response.data should have one record
            print(driver_data)
            return   {
                    "id": driver_data['ID'],
                    "name": driver_data.get('Name'),
                    "vehicle_num": driver_data.get('Vehicle_Number'),
                    "vehicle_type": driver_data.get('Vehicle_Type'),
                    "curr_loc": driver_data.get('Current_Location'),
                    "is_active": driver_data.get('Is_Active')
                }
        else:
            return None
