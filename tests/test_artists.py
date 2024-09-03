from lib.artists import Artists

"""
Constructs an id, name, genre
"""
def test_construct():
    artist = Artists(1, "test_name", "test_genre")
    assert artist.id == 1
    assert artist.name == "test_name"
    assert artist.genre == "test_genre"

"""
Artists with equal contents are equal
"""
def test_compares():
    artist_1 = Artists(1, "test_name", "test_genre")
    artist_2 = Artists(1, "test_name", "test_genre")
    assert artist_1 == artist_2

"""
Artists can be represented as strings
"""
def test_string():
    artist = Artists(1, "test_name", "test_genre")
    assert str(artist) == "Artists(1, test_name, test_genre)"


