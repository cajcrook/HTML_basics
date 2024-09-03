import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

from lib.album_repository import AlbumRepository
from lib.album import Album

from lib.artists_repository import ArtistRepository
from lib.artists import Artists

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

### ALBUMS

@app.route('/albums')
def html_albums_all():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums.html", albums=albums) 



@app.route('/albums/<int:id>')     
def find_html_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    if album:
        return render_template("show.html", album=album)
    else:
        return "Album not found", 404




# @app.route("/albums/<id>")
# def get_album(id):
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = repository.find(id)
#     return render_template ("show.html", album=album)



# @app.route('/albums')
# def get_albums():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)  
#     albums = repository.all()
#     return "\n".join(
#         f"{album}" for album in albums)


@app.route('/albums', methods = ['POST'])
def post_albums():
    if has_invalid_album_parameters(request.form):
        return "You need to submit a title, release_year and artist_id", 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)  
    album = Album(None, request.form['title'],
                  request.form['release_year'],
                  request.form['artist_id']
    )
    repository.create(album)
    return '', 200


def has_invalid_album_parameters(form):
    return 'title' not in request.form or \
    'release_year' not in request.form or \
        'artist_id' not in request.form

### ARTISTS

# @app.route('/artists')
# def get_artists():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)  
#     artists = repository.all()
#     return "\n".join(
#         f"{artist}" for artist in artists
#     )

@app.route('/artists', methods = ['POST'])
def post_artists():
    if has_invalid_artists_parameters(request.form):
        return "You need to submit a name and genre", 400
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)  
    artists = Artists(None, request.form['name'],
                  request.form['genre'])
    repository.create(artists)
    return '', 200


@app.route('/artists')
def html_artists_all():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template("artists.html", artists=artists) 


@app.route('/artists/<int:id>')     
def find_html_artists(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.find(id)
    if artists:
        return render_template("show_artists.html", artists=artists)
    else:
        return "artist not found", 404








def has_invalid_artists_parameters(form):
    return 'name' not in request.form or 'genre' not in request.form

from example_routes import apply_example_routes
apply_example_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))




