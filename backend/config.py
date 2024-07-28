# config.py

import os
from supabase import create_client, Client

# Load environment variables from .env file

# Initialize the Supabase client using environment variables
url: str = "variable"
key: str = "key"
supabase: Client = create_client(url, key)


# Expose the supabase client
def get_supabase_client():
    return supabase
