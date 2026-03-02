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

    is_active = Column(Boolean, nullable=False, default=True)
    is_verified = Column(Boolean, nullable=False, default=False)
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

# from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Table
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func
# from sqlalchemy.orm import declarative_base

# Base = declarative_base()

# # Association table for many-to-many relationship between users and roles
# user_roles = Table(
#     'user_roles',
#     Base.metadata,
#     Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE')),
#     Column('role_id', Integer, ForeignKey('roles.id', ondelete='CASCADE'))
# )


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True, nullable=False)
#     username = Column(String, unique=True, index=True, nullable=False)
#     full_name = Column(String)
#     hashed_password = Column(String, nullable=False)
#     is_active = Column(Boolean, default=True)
#     is_verified = Column(Boolean, default=False)
#     is_superuser = Column(Boolean, default=False)
    
#     # OAuth fields
#     oauth_provider = Column(String, nullable=True)  # google, github, etc.
#     oauth_id = Column(String, nullable=True)
    
#     # Timestamps
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), onupdate=func.now())
#     last_login = Column(DateTime(timezone=True), nullable=True)
    
#     # Relationships
#     roles = relationship("Role", secondary=user_roles, back_populates="users")
#     refresh_tokens = relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")


# class Role(Base):
#     __tablename__ = "roles"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, nullable=False)
#     description = Column(String)
    
#     # Timestamps
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
    
#     # Relationships
#     users = relationship("User", secondary=user_roles, back_populates="roles")
#     permissions = relationship("Permission", back_populates="role", cascade="all, delete-orphan")


# class Permission(Base):
#     __tablename__ = "permissions"

#     id = Column(Integer, primary_key=True, index=True)
#     role_id = Column(Integer, ForeignKey("roles.id", ondelete='CASCADE'), nullable=False)
#     resource = Column(String, nullable=False)  # e.g., "users", "posts"
#     action = Column(String, nullable=False)    # e.g., "read", "write", "delete"
    
#     # Relationships
#     role = relationship("Role", back_populates="permissions")


# class RefreshToken(Base):
#     __tablename__ = "refresh_tokens"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
#     token = Column(String, unique=True, nullable=False)
#     expires_at = Column(DateTime(timezone=True), nullable=False)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
    
#     # Relationships
#     user = relationship("User", back_populates="refresh_tokens")
