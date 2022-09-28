import asyncio

from src.controllers.user import users_crud
from src.controllers.product import products_crud
from src.controllers.address import addresses_crud
# from src.controllers.cart import cart_crud

loop = asyncio.get_event_loop()
loop.run_until_complete(users_crud())
#loop.run_until_complete(products_crud())
loop.run_until_complete(addresses_crud())