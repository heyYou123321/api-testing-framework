# tests/conftest.py
import pytest
import logging

@pytest.fixture
def get_data_status_code():
    return {
         "expected_status_code": 200
    }

@pytest.fixture
def get_data():
    return {
        "expected_response": {
            "id": 2,
            "userId": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        },
        "expected_status_code": 200    
    }

@pytest.fixture
def post_data():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 2
    }

@pytest.fixture
def post_data_status_code():
    return {
         "expected_status_code": 201
    }



class GET:
    get_data

class post:
    post_data
 

# Test data for various method types
test_data = {
    "GET": {
        "endpoint": "/posts/1",
        "expected_response": {
            "id": 2,
            "userId": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        },
        "expected_status_code": 200  
    },
    "POST": {
        "endpoint": "/posts",
        "request_data": {
            "userId": 1,
            "title": "foo",
            "body": "bar"
        },
        "expected_response": {
            "title": "foo",
            "body": "bar",
            "userId": 2 
        }
    }
}


@pytest.fixture
def setup(request):
    """
    Fixture that sets up the test data based on the API method type (GET, POST, etc.)
    and handles any teardown actions after the test.

    Usage:
        - This fixture detects the test function's method type and returns the relevant test data.
    """
    method_marker = request.node.get_closest_marker("method")  # Custom pytest marker to detect method type

    # Test data for various method types
    test_data = {
        "GET": {
            "endpoint": "/posts/1",
            "expected_response": {
                "id": 1,
                "userId": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
            },
            "expected_status_code": 200  
        },
        "POST": {
            "endpoint": "/posts",
            "request_data": {
                "userId": 1,
                "title": "foo",
                "body": "bar"
            },
            "expected_response": {
                "title": "foo",
                "body": "bar",
                "userId": 2 
            }
        }
    }

    if method_marker:
        method_type = method_marker.args[0]  # Extract the method type (GET, POST, etc.)
        logging.info(f"Setting up test data for method: {method_type}")

        # Fetch the test data based on the method type
        if method_type in test_data:
            yield test_data[method_type]
        else:
            raise ValueError(f"Unsupported HTTP method: {method_type}")
    else: 
        raise ValueError("invalid internal test config")


## the solution is the be able to get applied to both of the 
## apis repos that the Marketplace intelligence team supports