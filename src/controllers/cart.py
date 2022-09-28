from src.models.cart import (
    create_cart,
    get_cart,
    get_user_cart,
    delete_cart,
)
from src.models.user import get_user_by_email
from src.server.database import connect_db, db, disconnect_db

from bson.objectid import ObjectId

async def carts_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    carts_collection = db.carts_collection
    users_collection = db.users_collection

    item = {
        "product" : 
            {
                "name" : "Fritadeira Elétrica sem Óleo/Air Fryer Nell Fit - Preto 3,2L com Timer",
                "description" : "A fritadeira elétrica Nell Fit é um eletroportátil que não pode faltar na sua cozinha. O produto proporciona uma alimentação mais saudável, pois não utiliza óleo/Air Fryer em seu processo de cozimento. A fritadeira na cor preta é compacta e produzida em PP, ocupando menos espaço, possui luz indicadora de funcionamento, controle de temperatura, cesta removível antiaderente, capacidade total de 4,2L e cesto com capacidade de 3,2L. Sua alça fria garante maior segurança ao manusear a fritadeira e além disso, ela possui timer de 30 minutos sonoro e com desligamento automático. Agora é só preparar batatinha frita, coxinha, bolinha de queijo e pastel na sua fritadeira elétrica!",
                "price" : 369.0,
                "image" : "https://a-static.mlcdn.com.br/800x560/fritadeira-eletrica-sem-oleo-air-fryer-nell-fit-preto-32l-com-timer/magazineluiza/222479100/64ef4d6200a6efc6cce6d265588910a9.jpg",
            },
        "quantity" : 1
    }

    _id = ObjectId("6333edd7e66aa37f2fc806c8")
    user_email = "lu_domagalu@gmail.com"

    if option == '1':
        # create cart
        user = await get_user_by_email(
            users_collection,
            user_email
        )

        check_cart = await get_user_cart(
            carts_collection,
            user
        )
        print(check_cart)

        if check_cart:
            pass
            # new_cart = await add_address(
            #     addresses_collection,
            #     user,
            #     address
            # )

        else:
            first_cart = await create_cart(
                carts_collection,
                user,
                item, 
                item['product']['price'], 
                1
        )

    elif option == '2':
        # get cart by id
        cart = await get_cart(
            carts_collection,
            _id
        )
        print(cart)

    elif option == '3':
        # get cart by user 
        user = await get_user_by_email(
            users_collection,
            user_email
        )
        address = await get_user_cart(
            carts_collection,
            user
        )
        print(address)

    elif option == '4':
        # delete
        result = await delete_cart(
            carts_collection,
            _id,
        )
        print(result)

    await disconnect_db()
