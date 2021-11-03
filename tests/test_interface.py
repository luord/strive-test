import pytest

from quiz import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_root(client):
    res = client.get("/")

    assert b"Hello world" in res.get_data()
