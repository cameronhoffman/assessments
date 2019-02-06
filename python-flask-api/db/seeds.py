from peewee import *

from models import Item, ItemList

# Delete the table data.
Item.delete().execute()
ItemList.delete().execute()

# Create the initial item list
item_list = ItemList(name='Main List')
item_list.save()

# Create items under the item list
Item(name='Clean the room', item_list=item_list.id).save()
Item(name='Take out the trash', item_list=item_list.id).save()
Item(name='Sweep the floors', item_list=item_list.id).save()
