from sqlalchemy import Column, String, Integer
from src.infra.adapters.database.orm.models import Base


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    about = Column(String)

    def __init__(self, username, email, about=""):
        self.username = username
        self.email = email
        self.about = about
