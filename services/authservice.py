from database import db_session
from sqlalchemy.orm import Session
from models import User
from security.security import encrypting_password, decrypting_paramter, public_key, private_key
from fastapi import HTTPException
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.core.config import settings

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
            return None
        if encrypt_pass != password:
            return None
        return check_user
    
    def create_tokens(user_id: int) -> dict:
        """Create access and refresh tokens"""
        access_token = create_access_token(data={"sub": user_id})
        refresh_token = create_refresh_token(data={"sub": user_id})
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """Create JWT access token"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode.update({"exp": expire, "type": "access"})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt


    def create_refresh_token(data: dict) -> str:
        """Create JWT refresh token"""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode.update({"exp": expire, "type": "refresh"})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt
        

