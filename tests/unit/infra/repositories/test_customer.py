import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, NoResultFound

from src.domain.models import CustomerRequest
from src.infra.adapters.database.orm.models.customer import Customer
from src.infra.repositories.customer import insert_customer_repo, get_customer_by_id_repo, delete_customer_repo, update_customer_repo


@pytest.mark.asyncio()
@pytest.mark.usefixtures("setup_database")
async def test_insert_customer_when_request_is_valid_then_return_customer(session):
    # arrange
    valid_customer = Customer(username="John doe dev", email="johndoedev@teste.com", about="about me")

    # act
    with session() as session:
        customer_id = await insert_customer_repo(customer=valid_customer, session=session)

    # assert
    assert customer_id


@pytest.mark.asyncio()
@pytest.mark.usefixtures("setup_database")
async def test_insert_customer_when_insert_duplicated_key_then_raises_exception(session):
    # arrange
    duplicated_customer = Customer(username="John doe", email="john@teste.com", about="about me test")

    # act
    with session() as session:
        with pytest.raises(IntegrityError) as ex:
            await insert_customer_repo(customer=duplicated_customer, session=session)

    # assert
    assert ex.typename == "IntegrityError"


@pytest.mark.asyncio()
@pytest.mark.usefixtures("setup_database")
async def test_get_customer_when_id_exists(session):
    # arrange
    customer_id = 1

    # act
    with session() as session:
        customer = await get_customer_by_id_repo(id_=customer_id, session=session)

    # assert
    assert customer.username == "John doe"
    assert customer.email == "john@teste.com"
    assert customer.about == "about me test"


@pytest.mark.asyncio()
@pytest.mark.usefixtures("setup_database")
async def test_get_customer_when_id_doesnt_exists_then_raises_exception(session):
    # arrange
    customer_id = 2

    # act
    with session() as session:
        with pytest.raises(NoResultFound) as ex:
            await get_customer_by_id_repo(id_=customer_id, session=session)

    # assert
    assert ex.typename == "NoResultFound"


@pytest.mark.asyncio()
@pytest.mark.usefixtures("setup_database")
async def test_delete_customer_when_id_exists(session):
    # arrange
    customer_id = 1

    # act
    with session() as session:
        await delete_customer_repo(id_=customer_id, session=session)

        with pytest.raises(NoResultFound) as ex:
            statement = session.execute(select(Customer).filter_by(id=customer_id))
            statement.scalars().one()

        # assert
        assert ex.typename == "NoResultFound"


@pytest.mark.asyncio()
@pytest.mark.usefixtures("setup_database")
async def test_delete_customer_when_id_doesnt_exists_then_raises_exception(session):
    # arrange
    customer_id = 2

    # act
    with session() as session:
        with pytest.raises(NoResultFound) as ex:
            await delete_customer_repo(id_=customer_id, session=session)

    # assert
    assert ex.typename == "NoResultFound"


@pytest.mark.asyncio()
@pytest.mark.usefixtures("setup_database")
async def test_update_customer_when_id_exists(session):
    # arrange
    customer_id = 1
    customer_update = CustomerRequest(
        username="Naruto Uzumaki",
        email="narutinho@teste.com",
        about="Sou da vila da folha, to certo!"
    )

    # act
    with session() as session:
        await update_customer_repo(id_=customer_id, customer=customer_update, session=session)
        statement = session.execute(select(Customer).filter_by(id=customer_id))
        customer = statement.scalars().one()

    # assert
    assert customer.username == "Naruto Uzumaki"
    assert customer.email == "narutinho@teste.com"
    assert customer.about == "Sou da vila da folha, to certo!"


@pytest.mark.asyncio()
@pytest.mark.usefixtures("setup_database")
async def test_update_customer_when_id_doesnt_exists_then_raises_exception(session):
    # arrange
    customer_id = 2
    customer_update = CustomerRequest(
        username="Naruto Uzumaki",
        email="narutinho@teste.com",
        about="Sou da vila da folha, to certo!"
    )

    # act
    with session() as session:
        with pytest.raises(NoResultFound) as ex:
            await update_customer_repo(id_=customer_id, customer=customer_update, session=session)

    # assert
    assert ex.typename == "NoResultFound"
