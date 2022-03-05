def test_play_a_card(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'lastPlayed': '0'}
    response = client.put('/', json={'lastPlayed': '1'})
    assert response.json == {'lastPlayed': '1'}
    response = client.get('/')
    assert response.json == {'lastPlayed': '1'}
