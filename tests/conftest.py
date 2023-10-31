"""
Test module to define fixtures

"""
from flask import Flask
from flask.testing import FlaskClient
import pytest
from typing import Generator


@pytest.fixture(scope="module")
def test_client() -> Generator[FlaskClient, None, None]:
    
    # This can be changed once we have created our app
    app: Flask = None # create_app()

    with app.test_client() as test_client:
        yield test_client