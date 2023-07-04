from sqlalchemy.exc import IntegrityError, OperationalError, NoResultFound

from src.domain.models.customer import CustomerRequest
from src.infra.adapters.database.orm.models.customer import Customer
from sqlalchemy import select, update

from src.infra.adapters.database.orm.settings import Session


async def insert_customer_repo(customer: CustomerRequest, session: Session):
    try:
        new_customer = Customer(
            username=customer.username,
            email=customer.email,
            about=customer.about
        )
        session.add(new_customer)
        session.commit()
        return new_customer.id
    except Exception:
        raise


async def delete_customer_repo(id_: int, session):
    try:
        statement = session.execute(select(Customer).filter_by(id=id_))
        customer = statement.scalars().one()
        session.delete(customer)
        session.commit()
    except Exception:
        raise


async def update_customer_repo(id_: int, customer: CustomerRequest, session):
    try:
        await get_customer_by_id_repo(id_=id_, session=session)

        session.execute(update(Customer).where(Customer.id == id_).values({
            Customer.username: customer.username,
            Customer.email: customer.email,
            Customer.about: customer.about
        }))

        session.commit()
    except Exception:
        raise


async def get_customer_by_id_repo(id_: int, session):
    try:
        statement = session.execute(select(Customer).filter_by(id=id_))
        customer = statement.scalars().one()
        return customer
    except Exception:
        raise
