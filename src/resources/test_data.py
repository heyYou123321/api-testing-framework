# fixtures/test_data.py
test_data = {
    "test_get_resource": {
        "expected_response": {
            "id": 1,
            "userId": 1,
            "title": "qsunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        },
        "expected_status_code": 201
    },
    "test_posts_resource": {
        "expected_response": {
            "title": "foo",
            "body": "bar",
            "userId": 1
        },
        "expected_status_code": 201
    }
}
