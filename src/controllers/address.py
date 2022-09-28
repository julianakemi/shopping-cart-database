from src.models.address import (
    create_address,
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
        "district": "São Paulo",
        "city": "São Paulo",
        "state": "São Paulo",
        "is_delivery": True
    }

#    _id = ObjectId("")

    if option == '1':
        # create address
        user = await get_user_by_email(
            users_collection,
            "lu_domagalu@gmail.com"
        )

        address = await create_address(
            addresses_collection,
            user,
            address
        )
        print(address)

    # elif option == '2':
    #     # get_user_address
    #     address = await get_address(
    #         addresses_collection,
    #         _id
    #     )
    #     print(address)

    # elif option == '3':
    #     # get address by user email
    #     user_email = ""
    #     address = await get_user_address(
    #         addresses_collection,
    #         user_email
    #     )
    #     print(address)

    # elif option == '4':
    #     # delete
    #     result = await remove_address(
    #         addresses_collection,
    #         _id,
    #     )
    #     print(result)

    await disconnect_db()
