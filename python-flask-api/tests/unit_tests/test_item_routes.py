from flask import json
from peewee import *
import pytest

from db import seed
from models import ItemList, Item

from main import app

client = app.test_client()

class TestItemRoutes:
    @classmethod
    def setup_method(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        seed()

    def test_get_all_items_for_list(self):
        itemlist_id = ItemList.select().get().id

        response = client.get('/lists/{}/items'.format(itemlist_id))
        items = json.loads(response.data)
        assert len(items) == 3

    def test_create_item_success(self):
        body = { 'name': 'Test' }
        response = client.post('/items', json=body)
        item = json.loads(response.data)
        assert item['name'] == 'Test'

    def test_create_item_failure(self):
        body = { 'name': None }
        response = client.post('/items', json=body)

        with pytest.raises(Exception):
            item = json.loads(response.data)

    def test_update_item_success(self):
        item_id = Item.select().get().id

        body = { 'name': 'Test' }
        response = client.put('/items/{}'.format(item_id), json=body)
        item = json.loads(response.data)
        assert item['name'] == 'Test'

    def test_update_item_failure(self):
        item_id = Item.select().get().id

        body = { 'name': None }
        response = client.put('/items/{}'.format(item_id), json=body)

        with pytest.raises(Exception):
            item = json.loads(response.data)

    def test_delete_item(self):
        item_id = Item.select().get().id

        client.delete('/items/{}'.format(item_id))
        with pytest.raises(DoesNotExist):
            assert Item.get_by_id(item_id)
