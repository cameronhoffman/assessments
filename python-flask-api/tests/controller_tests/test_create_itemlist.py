from peewee import *
import pytest

from controllers import create_itemlist
from db import seed

def test_create_itemlist_success():
    seed()
    body = { 'name': 'Test' }
    itemlist = create_itemlist(body)
    assert itemlist.name == 'Test'

def test_create_itemlist_failure():
    seed()
    body = { 'name': None }

    with pytest.raises(IntegrityError):
        itemlist = create_itemlist(body)
