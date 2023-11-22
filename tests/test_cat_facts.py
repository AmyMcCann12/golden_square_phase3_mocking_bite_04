from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_returns_a_cat_fact():
    requester_mock = Mock()
    requester_mock.get().json.return_value = {
        "fact":"Tigers are excellent swimmers and do not avoid water."
        }
    cat_facts = CatFacts(requester_mock)
    assert cat_facts.provide() == "Cat fact: Tigers are excellent swimmers and do not avoid water."