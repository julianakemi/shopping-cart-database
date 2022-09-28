import asyncio

from src.controllers.user import users_crud
from src.controllers.product import products_crud
from src.controllers.address import addresses_crud
from src.controllers.cart import carts_crud

loop = asyncio.get_event_loop()

option = input("\nSelect an option:\n 1 - Users\n 2 - Products\n 3 - Addresses\n 4 - Carts\n 5 - Exit\n")
if option == '1':
    loop.run_until_complete(users_crud())
elif option == '2':
    loop.run_until_complete(products_crud())
elif option == '3':
    loop.run_until_complete(addresses_crud())
elif option == '4':
    loop.run_until_complete(carts_crud())
elif option == '5':
    exit()
