"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Bootstrap Page" in response.data
