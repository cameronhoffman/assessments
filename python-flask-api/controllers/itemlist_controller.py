from models import ItemList

def get_all_itemlists():
    return ItemList.select()

def create_itemlist(body):
    return ItemList.create(
        name=body['name']
    )
