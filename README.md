Here’s a draft of the README for your API testing framework project:

---

# API Testing Framework

This project is a Python-based API testing framework designed to automate the testing of APIs. The framework integrates Swagger/OpenAPI specifications to auto-generate tests, making it flexible and reusable for multiple APIs.

## Features

- **Automated Test Generation from Swagger/OpenAPI Specifications**: Automatically generates API tests based on the provided Swagger/OpenAPI specification file.
- **Customizable Assertions**: Provides utility functions for asserting status codes, JSON structures, and response data.
- **Support for Multiple HTTP Methods**: Currently supports GET, POST, PUT, and DELETE methods.
- **HTML Reports**: Generates detailed HTML reports for test execution.
- **Modular Structure**: Clean, modular project structure to allow easy integration and customization.

## Tech Stack

- **Python 3.12**
- **Pytest**: For test execution and reporting.
- **Requests**: To handle HTTP requests.
- **Swagger/OpenAPI**: For automated test generation.
- **pytest-html**: For generating HTML test reports.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/api-testing-framework.git
   cd api-testing-framework
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Docker Setup (optional):**
   If you prefer to run the tests in a containerized environment, build the Docker image:
   ```bash
   docker build -t api-testing-framework .
   ```

## Usage

### Running Tests

1. **Run all tests:**
   ```bash
   pytest
   ```

2. **Run specific tests:**
   To run tests with a specific marker (like `api`):
   ```bash
   pytest -m api
   ```

3. **Running via Docker:**
   To run tests inside Docker, use the following command:
   ```bash
   docker run --rm -v $(pwd)/reports:/app/reports api-testing-framework
   ```

### Swagger Test Generation

1. **Place Swagger File**: 
   Add your `swagger.json` file to the `src/swagger/` directory.
   
2. **Generate Tests**:
   Tests will be auto-generated from the `swagger.json` file during test execution, covering all the defined API paths and methods.

### Example API Test

```python
@pytest.mark.api
def test_get_resource():
    response = RequestUtil.get("/posts/1")
    assert_status_code(response, 200)
    expected_response = {
        "id": 1,
        "userId": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit..."
    }
    assert_json_structure(response.json(), expected_response)
```

## Directory Structure

```
api-testing-framework/
│
├── src/
│   ├── helpers/
│   │   ├── assertion_util.py
│   │   ├── request_util.py
│   ├── tests/
│   │   ├── integration_test/
│   │   ├── swaggerMagic/
│   │   ├── test_api.py
│   └── swagger/
│       └── swagger.json
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md
```

## Customization

- **Request Utilities**: Customize HTTP request logic in `src/helpers/request_util.py`.
- **Assertion Utilities**: Add or modify assertion logic in `src/helpers/assertion_util.py`.
- **Swagger Integration**: Modify test generation logic in `src/tests/swaggerMagic/swaggerParser.py`.

## Contributing

Feel free to submit pull requests or report issues. Contributions are welcome to improve test generation, expand HTTP method support, or enhance assertions.

---

Let me know if you'd like to add or modify anything!