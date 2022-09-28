from src.models.product import (
    create_product,
    get_product,
    get_products,
    update_product,
    delete_product
)
from src.server.database import connect_db, db, disconnect_db

from bson.objectid import ObjectId

async def products_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    products_collection = db.products_collection

    product =  {
        "name" : "Fritadeira Elétrica sem Óleo/Air Fryer Nell Fit - Preto 3,2L com Timer",
        "description" : "A fritadeira elétrica Nell Fit é um eletroportátil que não pode faltar na sua cozinha. O produto proporciona uma alimentação mais saudável, pois não utiliza óleo/Air Fryer em seu processo de cozimento. A fritadeira na cor preta é compacta e produzida em PP, ocupando menos espaço, possui luz indicadora de funcionamento, controle de temperatura, cesta removível antiaderente, capacidade total de 4,2L e cesto com capacidade de 3,2L. Sua alça fria garante maior segurança ao manusear a fritadeira e além disso, ela possui timer de 30 minutos sonoro e com desligamento automático. Agora é só preparar batatinha frita, coxinha, bolinha de queijo e pastel na sua fritadeira elétrica!",
        "price" : 369.0,
        "image" : "https://a-static.mlcdn.com.br/800x560/fritadeira-eletrica-sem-oleo-air-fryer-nell-fit-preto-32l-com-timer/magazineluiza/222479100/64ef4d6200a6efc6cce6d265588910a9.jpg",
    }

    _id = ObjectId("63324ab861759eaa10304dd5")

    if option == '1':
        # create product
        product = await create_product(
            products_collection,
            product
        )
        print(product)
        
    elif option == '2':
        # get product
        product = await get_product(
            products_collection,
            _id
        )
        print(product)

    elif option == '3':
        # update
        product_data = {
            "price" : 450.0,
        }

        is_updated, numbers_updated = await update_product(
            products_collection,
            _id,
            product_data
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")

    elif option == '4':
        # delete
        result = await delete_product(
            products_collection,
            _id,
        )
        print(result)

    elif option == '5':
        # pagination
        products = await get_products(
            products_collection,
            skip=0,
            limit=6
        )
        print(products)

    await disconnect_db()
