from playwright.sync_api import Page, expect

# Tests for your routes go here

"""Test GET /albums route that returns all albums in database
return should be HTML
"""
def test_html_albums_all(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    li_tag = page.locator("li")
    expect(li_tag).to_have_text([
        "What Went Down",
        "Humbug",
        "Singles"    
        ])
    

"""
Test GET /albums/2 find_album with id 
"""

def test_find_html_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Title: What Went Down") 
    release_year_tag = page.locator("p:has-text('Release: 2015')")
    expect(release_year_tag).to_have_text("Release: 2015")




def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='What Went Down'")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Title: What Went Down") 
    release_year_tag = page.locator(".t-release-year")
    expect(release_year_tag).to_have_text("Release: 2015")


def test_back_button(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='What Went Down'")
    page.click("text='BACK'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

##### ARTISTS


"""Test GET /albums route that returns all albums in database
return should be HTML
"""
def test_html_artists_all(page, test_web_address, db_connection):
    db_connection.seed("seeds/artists.sql")
    page.goto(f"http://{test_web_address}/artists")
    li_tag = page.locator("li")

    # Get the text of each <li> element and strip the whitespace
    actual_texts = li_tag.all_text_contents()
    actual_texts = [text.strip() for text in actual_texts]

    # Normalize the case of the text
    actual_texts = [text.lower() for text in actual_texts]

    expected_texts = ["pixies", "abba", "taylor swift", "nina simone"]

    # Assert that the normalized and stripped actual texts match the expected
    assert actual_texts == expected_texts

"""
Test GET /albums/2 find_album with id 
"""
def test_find_html_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/artists.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Name: Pixies") 
    release_year_tag = page.locator("p:has-text('Genre: Rock')")
    expect(release_year_tag).to_have_text("Genre: Rock")

# # === End Example Code ===
