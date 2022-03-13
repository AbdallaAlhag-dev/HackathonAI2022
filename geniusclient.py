# problems thus far
# Embed message, titles are showing, despacito is in spanish we need english lyrics

# Library to access content on Genius.com
import lyricsgenius as lg

# Search and manipulate strings
import re

# We retrieve data from the Genius API using the LyricsGenius python module
api = lg.Genius('mG0s2LL-EdEB-YDZvpf3bE2WjXuDdple7riOw5cEn5T_zM8RsbXGPL5LyfgWwnMw',
		skip_non_songs=True, verbose=False, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

def lyrics_scraper(genre):

    # Write to file
    file = open("geniuslyrics.txt", 'w')

    # Getting lyrics of songs by genre
    page = 2 
    while page < 4:
        # Try Except statements to handle when a timeout occurs
        try:
            results = api.tag(genre, page=page)
            for hit in results['hits']:
                song_lyrics = api.lyrics(song_url=hit['url'], )
                file.write(song_lyrics)
                file.write('\n\n')
            page = results['next_page']      
        except:
            pass

    file.close()


