
def test_hashtag_save(client):
    import json

    data = {'hashtags': '#teste'}

    response = client.post(
        '/hashtag/save',
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )

    content = json.loads(response.data)

    assert response
    # assert response.status_code == 200
    # assert response.status_coode == 201

    # assert content['success'] == True

def test_hashtag_retrieve(client):
    import json

    response = client.get(
        '/hashtag/retrieve',
        headers={'Content-Type': 'application/json'}
    )

    assert response
    assert response.status_code == 200

    # content = json.loads(response.data)
    # assert type(content['data']) is list