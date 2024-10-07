
# src/helpers/assertion_util.py
import logging

def assert_status_code(response_json, expected_status):
    logging.info(f"assert_status_code Response Body: {response_json}")
    assert response_json.status_code == expected_status, f"Expected {expected_status}, got {response_json.status_code}"

def assert_json_key(response_json, key):
    logging.info(f"assert_json_key Response values actual: {response_json.json()}")
    assert key in response_json.json(), f"Key '{key}' not found in the response"

def assert_json_value(response_json, key, expected_json):
    logging.info(f"assert_json_value Response values actual: {response_json[key]}, expected: {expected_json}")
    assert response_json[key] == expected_json, f"Expected {expected_json} for '{key}', got {response_json.get(key)}"

def assert_json_structure(response_json, expected_json):
    for key, expected_value in expected_json.items():
        logging.info(f"assert_json_structure Response values actual: {response_json[key]}, expected: {expected_json[key]}")
        assert response_json.get(key) == expected_value, f"Expected {expected_value} for '{key}', got {response_json.get(key)}"


#what additional assertion utilities can we write?