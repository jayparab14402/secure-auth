from models import User
from database import db_session
from fastapi import HTTPException, status
from security.security import encrypting_password, decrypting_paramter, read_keys

class Users:
    """Get user by email"""
    def check_user_by_email(db, email):
            return db.query(User).filter(User.email == email).first()
    """Get user by username"""
    def check_user_by_username(db, uname):
            return db.query(User).filter(User.username == uname).first()
    """Get user by ID"""
    def check_user_by_id(db, user_id):
            return db.query(User).filter(User.id == user_id).first()
    """Create new user"""
    def create_user(db, user_data):
        
        if Users.check_user_by_email(db_session, user_data.email):
              raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User already exists"
              )
        
        if Users.check_user_by_username(db_session, user_data.username):
              raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User already exists"
              )
        
        encrypt_password = encrypting_password(user_data.password)

        """Store the data into db"""
        
        

        
