import json


def test_reverse_endpoint(client):
    response = client.get("/example")
    response_data = json.loads(response.data)
    assert response.status_code == 200
    assert 'result' in response_data
    assert response_data['result'] == 'elpmaxe'
