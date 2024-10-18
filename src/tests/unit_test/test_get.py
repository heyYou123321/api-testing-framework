from helpers.assertion_util import assert_json_structure, assert_json_value, assert_status_code
from helpers.request_util import RequestUtil
import pytest
from unittest.mock import patch, Mock

# Sample expected response data
expected_response = {
    "id": 1,
    "userId": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
}

@pytest.mark.api
@patch('src.helpers.request_util.RequestUtil.get')  # Mocking the get method
def test_get_resource(mock_get):
    
    # Setting up the mock to return a Response-like object
    mock_response = Mock()
    mock_response.json.return_value = expected_response  # Mock the json() method
    mock_response.status_code = 200  # Mocking the status code

    mock_get.return_value = mock_response  # Return the mock response when get is called

    response = RequestUtil.get("/posts/1")  # This will call the mocked method
    assert_status_code(response, mock_response.status_code)

    # Now you can assert the values from the expected response
    assert_json_value(response.json(), "id", mock_response.json.return_value["id"])
    assert_json_value(response.json(), "userId", mock_response.json.return_value["userId"])
    assert_json_value(response.json(), "title", mock_response.json.return_value["title"])
    assert_json_structure(response.json(), mock_response.json.return_value)
