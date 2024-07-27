# config.py

import os
from supabase import create_client, Client

# Load environment variables from .env file

# Initialize the Supabase client using environment variables
url: str = "https://cdybixknwjhuogfbzxvv.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNkeWJpeGtud2podW9nZmJ6eHZ2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIwNjA3MjAsImV4cCI6MjAzNzYzNjcyMH0.4kZ26CQxeOtq5mLSzNnLX2X9GjtGpOhNHRTFGFi3p2c"
supabase: Client = create_client(url, key)


# Expose the supabase client
def get_supabase_client():
    return supabase
