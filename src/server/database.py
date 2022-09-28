from os import environ
from motor.motor_asyncio import AsyncIOMotorClient

class DataBase:
    client: AsyncIOMotorClient = None
    #database_uri = environ.get("DATABASE_URI")
    database_uri = 'mongodb+srv://julianakemide:88bBFYjQDNewGZ@luizacode.1cduc35.mongodb.net/?retryWrites=true&w=majority'
    users_collection = None
    addresses_collection = None
    products_collection = None
    orders_collection = None
    order_itens_collection = None
    carts_collection = None
    cart_itens_collection = None

db = DataBase()

async def connect_db():
    db.client = AsyncIOMotorClient(
        db.database_uri,
        minPoolSize = 10,
        maxPoolSize = 10,
        tls = True,
        tlsAllowInvalidCertificates = True
    )
    db.users_collection = db.client.shopping_cart.users
    db.addresses_collection = db.client.shopping_cart.addresses
    db.products_collection = db.client.shopping_cart.products
    db.orders_collection = db.client.shopping_cart.orders
    db.order_items_collection = db.client.shopping_cart.order_itens
    db.carts_collection = db.client.carts_collection
    db.cart_itens_collection = db.client.cart_itens_collection

    # try:
    #     print(await db.client.server_info())
    # except Exception:
    #     print("Unable to connect to the server.")

async def disconnect_db():
    db.client.close()