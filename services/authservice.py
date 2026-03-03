from database import db_session
from sqlalchemy.orm import Session
from models import User
from security.security import encrypting_password, decrypting_paramter, public_key, private_key
from fastapi import HTTPException

class AuthService:

    def authenticate_user(db: Session, email: str, password: str):
        '''take email pass in request
        query db to check for email
        if found verify the pass 
        and return the user if found else return none
        '''    
        print(f"Inside authenticate_user {email} {password}")
        check_user = db.query(User).filter(User.email == email).first()
        # print(f"After quering { if check_user else None}")
        if not check_user:
            print("Returned from not check_user")
            raise HTTPException(
                detail="No user found",
                status_code=400
            )
        encrypt_pass = decrypting_paramter(check_user.hashed_password, private_key)
        print(f"Encrypted pass {encrypt_pass}")
        if not encrypt_pass:
            print("Returned from not encrypt_pass")
            return "ok"
        if encrypt_pass == password:
            return check_user
        return "okyendrra"
