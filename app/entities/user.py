from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from app.entities import Base


class Users(Base):
    __tablename__ = "Users"
    UserId = Column(Integer, primary_key=True, nullable=False)
    UserName = Column(String, nullable=False, unique=True)
    UserEmail = Column(String, nullable=False, unique=True)
    UserPasswordHash = Column(String, nullable=False)
    UserAvatar = Column(String, nullable=False)
    UserActivationToken = Column(String, nullable=False)
    UserIsActive = Column(Boolean, nullable=False)
    UserEmailVerifiedAt = Column(TIMESTAMP(timezone=True),
                                 nullable=True, server_default=text('now()'))
    UserLastLoginAt = Column(TIMESTAMP(timezone=True),
                             nullable=True, server_default=text('now()'))
    CreatedAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=text('now()'))
    UpdatedAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=text('now()'))
