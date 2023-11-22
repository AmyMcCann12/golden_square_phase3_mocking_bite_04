from unittest.mock import Mock
from lib.time_error import TimeError

def test_calls_api_to_get_server_time():
    requester_mock = Mock()
    response_mock = Mock()
    comp_time_mock = Mock()
    comp_time_mock.time.return_value = 1700646380.5
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1700648065}
    time_error = TimeError(requester_mock, comp_time_mock)
    result = time_error.error()
    assert result == 1684.5