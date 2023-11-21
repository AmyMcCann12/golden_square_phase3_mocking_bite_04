from unittest.mock import Mock
from lib.activity_suggester import ActivitySuggester

"""
When we call suggest
It returns a nice activity for us to do
"""

def test_suggests_a_nice_activity():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get().json.return_value = {"activity":"Go to a concert with local artists with some friends","type":"social","participants":3,"price":0.4,"link":"","key":"2211716","accessibility":0.3}
    suggester = ActivitySuggester(requester_mock)
    assert suggester.suggest() == "Why not: Go to a concert with local artists with some friends"