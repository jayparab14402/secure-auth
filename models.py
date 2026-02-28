from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    func
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, nullable=False, index=True)
    username = Column(String, unique=True, nullable=False, index=True)

    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)

    is_active = Column(Boolean, nullable=True)
    is_verified = Column(Boolean, nullable=True)
    is_superuser = Column(Boolean, nullable=True)

    oauth_provider = Column(String, nullable=True)
    oauth_id = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True)
    )

    updated_at = Column(
        DateTime(timezone=True)
    )

    last_login = Column(
        DateTime(timezone=True)
    )