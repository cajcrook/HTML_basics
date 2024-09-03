from lib.album import Album

"""
Constructs an id, title, release_year and artist_id
"""
def test_contstruct():
    album = Album(1, "Test title", 1000, 2)
    assert album.id == 1
    assert album.title == "Test title"
    assert album.release_year == 1000
    assert album.artist_id == 2 

"""
Albums with identical contents are equal
"""
def test_compares():
    album_1 = Album(1, "Test title", 1000, 2)
    album_2 = Album(1, "Test title", 1000, 2)
    assert album_1 == album_2

"""
Albums can be represented as strings
"""
def test_stringifying():
    album = Album(1, "Test title", 1000, 2)
    assert str(album) == "Album(1, Test title, 1000, 2)"


