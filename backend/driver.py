# driver.py

from config import get_supabase_client

supabase = get_supabase_client()

class Driver:
    def __init__(self, id, name, vehicle_num, vehicle_type, curr_loc, is_active):
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
            "Vehicle Number": self.vehicle_num,
            "Vehicle Type": self.vehicle_type,
            "Current Location": self.curr_loc,
            "Is Active": self.is_active
        }

    def set_profile(self, name, vehicle_num, vehicle_type, curr_loc, is_active):
        self.name = name
        self.vehicle_num = vehicle_num
        self.vehicle_type = vehicle_type
        self.curr_loc = curr_loc
        self.is_active = is_active

    def save_to_db(self):
        data = self.get_profile()
        response = supabase.table('drivers').upsert(data).execute()
        return response

    @classmethod
    def fetch_from_db(cls, driver_id):
        response = supabase.table('drivers').select('*').eq('ID', driver_id).execute()
        data = response.data[0]
        return cls(
            id=data['ID'],
            name=data['Name'],
            vehicle_num=data['Vehicle Number'],
            vehicle_type=data['Vehicle Type'],
            curr_loc=data['Current Location'],
            is_active=data['Is Active']
        )

    def get_request(self, patient, hospital, is_emergency):
        return {
            "Patient": patient.get_profile(),
            "Hospital": hospital.get_details(),
            "Is Emergency": is_emergency
        }

    def action_on_request(self, is_accept, request_data):
        if is_accept:
            trip_data = {
                "Driver ID": self.id,
                "Patient ID": request_data['Patient']['ID'],
                "Hospital ID": request_data['Hospital']['ID'],
                "Start Location": request_data['Patient']['Current Location'],
                "End Location": request_data['Hospital']['Location'],
                "Is Emergency": request_data['Is Emergency']
            }
            response = supabase.table('trips').insert(trip_data).execute()
            return "Request accepted and trip started", response
        else:
            return "Request rejected"
