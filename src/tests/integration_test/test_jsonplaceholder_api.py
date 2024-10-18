
# src/tests/test_api.py

import pytest 
import logging
from resources.test_data import test_data
from src.helpers.request_util import RequestUtil
from src.helpers.assertion_util import assert_status_code, assert_json_key, assert_json_value, assert_json_structure

@pytest.mark.api
@pytest.mark.method("GET")
def test_get_resource(setup):

    try:
        get_data = setup  # This is the data yielded by the setup fixture

        # Accessing the expected response from the setup data
        logging.info(f"Test data Response Body: {get_data['expected_response']}")

        # Simulate the GET request
        response = RequestUtil.get(get_data["endpoint"])

        # Assert the status code
        assert_status_code(response, get_data["expected_status_code"])

        # Assert the JSON structure
        json_response = response.json()
        assert_json_structure(json_response, get_data["expected_response"])
    except ValueError:
        print("Oops! theres been an error. Look at log by setting log_cli to true in pytest.ini ")


# @pytest.mark.api
# @pytest.mark.parametrize("resource_id, expected_name", [
#     (1, "Resource Name 1"),
#     (2, "Resource Name 2"),
#     (3, "Resource Name 3"),
# ])
# def test_get_resources(resource_id, expected_name):
#     response = RequestUtil.get(f"/resource/{resource_id}")
#     assert_status_code(response, 200)
#     assert_json_key(response, "data")
#     assert_json_value(response, "data", {"id": resource_id, "name": expected_name})

@pytest.mark.api
def test_posts_resource():
    
    # Get the expected data from the test_data fixture
    expected_response = test_data["test_posts_resource"]["expected_response"]
    expected_status_code = test_data["test_posts_resource"]["expected_status_code"]


    response = RequestUtil.post("/posts",expected_response)
    assert_status_code(response, expected_status_code)

    # Assuming you're directly accessing the response here
    json_response = response.json()  # Get the JSON data
    logging.info(f"Response Status Code: {response.status_code}")
    assert_json_structure(json_response, expected_response)  # Compare the entire structure

# Example usage with pytest
if __name__ == "__main__":
    pytest.main(["-v"])
