from src.infra.adapters.orm.database.settings import Base
from sqlalchemy import Column, String, Integer


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email
