
async def create_first_address(addresses_collections, user, address):
    try:
        address = await addresses_collections.insert_one({'user': user, 'address': [address]})
        if address.inserted_id:
            address = await get_address(addresses_collections, address.inserted_id)
            return address
    except Exception as e:
        print(f'create_address.error: {e}')

async def add_address(addresses_collections, user, address):
    try:
        address = await addresses_collections.update_one(
            {'user': user},
            {'$addToSet': {'address': address}})
        if address.modified_count:
            return True, address.modified_count

        return False, address.modified_count
    except Exception as e:
        print(f'add_address.error: {e}')

async def get_address(addresses_collections, address_id):
    try:
        data = await addresses_collections.find_one({'_id': address_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')

async def get_user_address(addresses_collections, user):
    try:
        data = await addresses_collections.find_one({'user': user})
        if data:
            return data
    except Exception as e:
        print(f'get_user_address.error: {e}')


async def remove_address(addresses_collections, address_id):
    try: 
        address = await addresses_collections.delete_one({'_id': address_id})
        if address.deleted_count:
            return {'status': f'{address_id} deleted'}
    except Exception as e:
        print(f'remove_address.error: {e}')
