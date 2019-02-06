from peewee import *
import pytest

from controllers import create_itemlist, get_all_itemlists
from db import seed

class TestItemlistController:
    @classmethod
    def setup_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        seed()

    def test_get_all_lists(self):
        itemlists = get_all_itemlists()
        assert len(itemlists) == 2

    def test_create_itemlist_success(self):
        body = { 'name': 'Test' }
        itemlist = create_itemlist(body)
        assert itemlist.name == 'Test'

    def test_create_itemlist_failure(self):
        body = { 'name': None }

        with pytest.raises(IntegrityError):
            itemlist = create_itemlist(body)
