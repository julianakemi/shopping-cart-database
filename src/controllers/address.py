from src.models.address import (
    create_first_address,
    add_address,
    get_address,
    get_user_address,
    remove_address
)
from src.models.user import get_user_by_email
from src.server.database import connect_db, db, disconnect_db

from bson.objectid import ObjectId

async def addresses_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    addresses_collection = db.addresses_collection
    users_collection = db.users_collection

    address = {
        "street": "Rua Quarenta e Sete, Numero 3",
        "cep": "8465312",
        "district": "Mato Grosso",
        "city": "Cuiabá",
        "state": "MT",
        "is_delivery": True
    }

    _id = ObjectId("6333edd7e66aa37f2fc806c8")
    user_email = "lu_domagalu@gmail.com"

    if option == '1':
        # create address
        user = await get_user_by_email(
            users_collection,
            user_email
        )

        check_address = await get_user_address(
            addresses_collection,
            user
        )
        print(check_address)

        if check_address:
            new_address = await add_address(
                addresses_collection,
                user,
                address
            )

        else:
            first_address = await create_first_address(
                addresses_collection,
                user,
                address
            )

    elif option == '2':
        # get address by id
        address = await get_address(
            addresses_collection,
            _id
        )
        print(address)

    elif option == '3':
        # get address by user 
        user = await get_user_by_email(
            users_collection,
            user_email
        )
        address = await get_user_address(
            addresses_collection,
            user
        )
        print(address)

    elif option == '4':
        # delete
        result = await remove_address(
            addresses_collection,
            _id,
        )
        print(result)

    await disconnect_db()
