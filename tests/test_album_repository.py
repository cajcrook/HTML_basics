from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When I call #all
I get all teh albums in the album table
"""
def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, 'What Went Down', 2015, 1),
        Album(2, "Humbug", 2009, 2),
        Album(3, 'Singles', 2014, 3)
    ]

"""
When I call #find
I get an album based on the id
"""
def test_find(db_connection):
        db_connection.seed("seeds/record_store.sql")
        repository = AlbumRepository(db_connection)
        albums = repository.find(2)
        assert albums == Album(2, "Humbug", 2009, 2)

 

"""
When I call #create
I create an album in the database
And I can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "test", 1000, 4)
    repository.create(album)
    assert repository.all() == [
        Album(1, 'What Went Down', 2015, 1),
        Album(2, "Humbug", 2009, 2),
        Album(3, 'Singles', 2014, 3),
        Album(4, "test", 1000, 4)
        ]




