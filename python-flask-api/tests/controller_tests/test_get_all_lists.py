from controllers import get_all_itemlists
from db import seed

def test_get_all_lists():
    seed()
    itemlists = get_all_itemlists()
    assert len(itemlists) == 2
