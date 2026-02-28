import jwt
import traceback
from datetime import datetime as dt, timedelta

SECRET_KEY = "RWER$#T%Y^UTYT@ETGF543q"
ALGO = "HS256"

def generate_auth_token(data, expire_time):
    try:
        if not data:
            raise ValueError("Data needs to be passed")
        copied_data = data.copy()
        if expire_time:
            expire_time = dt.utcnow()
        expire_time = dt.utcnow() + timedelta(minutes=15)
        copied_data.update({"issued_time": dt.utcnow, "expire_time": expire_time})
        encoded_jwt = jwt.encode(copied_data, SECRET_KEY, ALGO)
        return encoded_jwt
    except Exception as e:
        print(f"Error in genarating auth token: {traceback.format_exc()}")
        return None
    
