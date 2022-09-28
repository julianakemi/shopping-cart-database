
async def create_address(addresses_collections, address, user):
    try:
        address = await addresses_collections.insert_one({'user': user}, {'address': [address]})
        if address.inserted_id:
            address = await get_address(addresses_collections, address.inserted_id)
            return address
    except Exception as e:
        print(f'create_address.error: {e}')

async def get_address(addresses_collections, address_id):
    try:
        data = await addresses_collections.find_one({'_id': address_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')

async def get_user_address(addresses_collections, user_email):
    try:
        data = list(await addresses_collections.find({'user': {'email': user_email}}))
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')


async def remove_address(addresses_collections, address_id):
    try: 
        address = await addresses_collections.delete_one({'_id': address_id})
        if address.deleted_count:
            return {'status': f'{address_id} deleted'}
    except Exception as e:
        print(f'remove_address.error: {e}')
