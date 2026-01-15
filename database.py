from sqlalchemy import create_engine, text, func
from sqlalchemy.orm import sessionmaker
from config import get_config
import traceback


secure_auth_db_creds = get_config("secureauthdb_creds")
engine = create_engine(f"postgresql://{secure_auth_db_creds['DB_USER']}:{secure_auth_db_creds['DB_PASS']}@{secure_auth_db_creds['DB_HOST']}:{secure_auth_db_creds['DB_PORT']}/{secure_auth_db_creds['DB_NAME']}")
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def db_session():
    try:
        db = session()
        yield db
    except Exception as e:
        print(f"Error in creating db connection: {traceback.format_exc()}")
    finally:
        db.close()
