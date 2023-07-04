import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infra.adapters.database.orm.models import Base
from src.infra.adapters.database.orm.models.customer import Customer

engine = create_engine('sqlite:///./test.db')


@pytest.fixture()
def session():
    return sessionmaker(bind=engine)


@pytest.fixture()
def setup_database(session):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    create_customer_test(session=session)


def create_customer_test(session):
    customer_test = Customer(
        username="John doe",
        email="john@teste.com",
        about="about me test"
    )

    with session() as session:
        session.add(customer_test)
        session.commit()
