"""
Test module to test api resources
"""
from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_example(test_client: FlaskClient) -> None:
    """
        This assumes a flask route in place.
    """
    response: TestResponse = test_client.get("/api/v1/example")

    assert response.status_code == 201
    assert response.text == "Hello from example"
