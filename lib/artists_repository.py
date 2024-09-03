from lib.artists import Artists

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM artists")
        return [Artists(row["id"], row["name"], row["genre"])
                for row in rows]
    
    def create(self, artists):
        self._connection.execute("INSERT INTO artists (name, genre) VALUES (%s, %s)",
                                 [artists.name, artists.genre])
        return None


    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from artists WHERE id = %s', [id])
        row = rows[0]
        return Artists(row["id"], row["name"], row["genre"])