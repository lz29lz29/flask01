"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/about")
    assert b"Rhoncus urna neque viverra" in response.data
