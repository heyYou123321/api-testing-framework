import json

from src.tests.integration_test.test_api import test_get_resource, test_posts_resource
from src.helpers.assertion_util import assert_json_structure, assert_status_code
from src.helpers.request_util import RequestUtil
import pytest
import requests
import logging
from openapi_spec_validator import validate_spec

# Load the Swagger file
def load_swagger_spec(file_path):
    with open(file_path) as swagger_file:
        swagger_spec = json.load(swagger_file)
    return swagger_spec

# Validate the Swagger spec
def validate_swagger_spec(swagger_spec):
    try:
        validate_spec(swagger_spec)
        print("Swagger specification is valid!")
    except Exception as e:
        raise Exception(f"Swagger validation error: {e}")

# Function to fetch posts and create an expected response object
def fetch_first_five_posts():
    expected_responses = []
    
    for post_id in range(1, 6):  # Loop through IDs 1 to 5
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        
        if response.status_code == 200:
            # Append the JSON response to the expected responses list
            expected_responses.append(response.json())
        else:
            print(f"Failed to fetch post with ID {post_id}. Status code: {response.status_code}")

    return expected_responses

# Fetch the expected response object
#expected_responses = fetch_first_five_posts()

# Helper function to dynamically generate test cases based on Swagger spec
def generate_tests_from_swagger(swagger_spec):
    paths = swagger_spec.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            yield path, method.upper(), details

# Dynamic test generation for pytest
@pytest.mark.parametrize("path,method,details", generate_tests_from_swagger(load_swagger_spec("swagger.json")))
def test_dynamic_api(path, method, details):
    print(f"Running test for {method} {path}")
    url = f"https://petstore.swagger.io/v2/{path}"
    logging.info(f"path in swagger: {path} with methods: {method} details: {details}")
    # Prepare request based on method type
    headers = {"Content-Type": "application/json"}
    request_data = {}  # Add request body data if necessary based on the details
    if 'requestBody' in details:
        request_data = details['requestBody']['content']['application/json']['schema']

    # Send the request based on the HTTP method
    if method == "GET":
        test_get_resource()

    elif method == "POST":
        test_posts_resource()
        #response = requests.post(url, headers=headers, json=request_data)
    elif method == "PUT":
        #response = requests.put(url, headers=headers, json=request_data)
        ...
    elif method == "DELETE":
        ...
        #response = requests.delete(url, headers=headers)


# Example usage with pytest
if __name__ == "__main__":
    pytest.main(["-v"])
