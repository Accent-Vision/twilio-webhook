from datetime import datetime

def log_call_details(caller_id):
    print(f"[{datetime.now()}] Incoming call from {caller_id}")