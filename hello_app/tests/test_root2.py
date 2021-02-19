from hello_app.tests import client

def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()
    assert landing.status_code == 200

def test_temperature(client):
    temperature = client.get("/temp")
    html = temperature.data.decode()
    print(html)
    assert type(html) == int