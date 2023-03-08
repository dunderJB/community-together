from sqlalchemy.exc import IntegrityError, OperationalError, NoResultFound

from src.domain.models.customer import CustomerRequest
from src.infra.adapters.orm.models.customer import Customer
from src.infra.adapters.orm.database.settings import Session
from sqlalchemy import select, update


async def insert_customer_repo(customer: CustomerRequest):
    with Session() as session:
        try:
            new_customer = Customer(username=customer.username, email=customer.email)
            session.add(new_customer)
            session.commit()
            return new_customer.id
        except IntegrityError:
            raise
        except OperationalError:
            raise
        except Exception:
            raise


async def delete_customer_repo(id_: int):
    with Session() as session:
        try:
            statement = session.execute(select(Customer).filter_by(id=id_))
            customer = statement.scalars().one()
            session.delete(customer)
            session.commit()
        except NoResultFound:
            raise
        except Exception:
            raise


async def update_customer_repo(id_: int, customer: CustomerRequest):
    with Session() as session:
        try:
            await get_customer_by_id_repo(id_=id_)

            session.execute(update(Customer).where(Customer.id == id_).values({
                Customer.username: customer.username,
                Customer.email: customer.email
            }))

            session.commit()
        except NoResultFound:
            raise
        except Exception:
            raise


async def get_customer_by_id_repo(id_: int):
    with Session() as session:
        try:
            statement = session.execute(select(Customer).filter_by(id=id_))
            customer = statement.scalars().one()
            return customer
        except NoResultFound:
            raise
        except OperationalError:
            raise
        except Exception:
            raise
