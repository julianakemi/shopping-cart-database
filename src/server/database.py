from os import environ
from motor.motor_asyncio import AsyncIOMotorClient

class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = environ.get("DATABASE_URI")
    users_collection = None
    addresses_collection = None
    products_collection = None
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
    db.carts_collection = db.client.shopping_cart.carts

    try:
        print(await db.client.server_info())
    except Exception:
        print("Unable to connect to the server.")

async def disconnect_db():
    db.client.close()