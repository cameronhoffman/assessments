from models import ItemList

def get_all_itemlists():
    return ItemList.select()
