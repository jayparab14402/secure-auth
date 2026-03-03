from models import User, Role
# from database import db_session
from fastapi import HTTPException, status
from security.security import encrypting_password, decrypting_paramter, public_key
from datetime import datetime as dt
from sqlalchemy.orm import Session
class Users:
    """Get user by email"""
    def check_user_by_email(db, email):
            print("Inside check_user_by_email")
            return db.query(User).filter(User.email == email).first()
    """Get user by username"""
    def check_user_by_username(db, uname):
            print("Inside check_user_by_username")
            
            return db.query(User).filter(User.username == uname).first()
    """Get user by ID"""
    def check_user_by_id(db, user_id):
            print("Inside check_user_by_id")
            
            return db.query(User).filter(User.id == user_id).first()
    """Create new user"""
    def create_user(user_data, db: Session):
        print("Inside create user")
        if Users.check_user_by_email(db, user_data.email):
              raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User already exists"
              )
        
        if Users.check_user_by_username(db, user_data.username):
              raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User already exists"
              )
        print("Before encrypting pass")
        encrypt_password = encrypting_password(user_data.password, public_key)
        print("After encrypting pass")
        
        """Store the data into db
        """
        db_record = User(
              email = user_data.email,
              username = user_data.username,
              full_name = user_data.full_name,
              hashed_password = encrypt_password,
              is_active=True,
              is_verified=True,
              created_at = dt.now(),
              updated_at = dt.now()
        )

        user_roles = db.query(Role).filter(Role.name == "user").first()
        if user_roles:
              db_record.roles.append(user_roles)
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        print("Record Commited")
        return db_record

        

        
