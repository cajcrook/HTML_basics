from lib.artists_repository import ArtistRepository
from lib.artists import Artists


"""
When I call artists # all
I get all the artists in the artists table
"""
def test_all(db_connection):
    db_connection.seed("seeds/artists.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
        Artists(1, 'Pixies', 'Rock'),
        Artists(2, 'ABBA', 'Pop'),
        Artists(3, 'Taylor Swift', 'Pop'),
        Artists(4, 'Nina Simone', 'Jazz')
    ]
                                  
"""
When I call #create 
I create a new artist in the database
and I can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/artists.sql")
    repository = ArtistRepository(db_connection)
    artists = Artists(None, "test_name", "test_genre")
    repository.create(artists)  
    assert repository.all() == [
        Artists(1, 'Pixies', 'Rock'),
        Artists(2, 'ABBA', 'Pop'),
        Artists(3, 'Taylor Swift', 'Pop'),
        Artists(4, 'Nina Simone', 'Jazz'),
        Artists(5, 'test_name', 'test_genre')
    ]


"""
When I call #find
I get an artist based on the id
"""
def test_find(db_connection):
        db_connection.seed("seeds/artists.sql")
        repository = ArtistRepository(db_connection)
        artists = repository.find(2)
        assert artists == Artists(2, 'ABBA', 'Pop')



