import webbrowser
import os
import re
import csv
import media


def get_template(to_get):
    file_to_get = 'templates/' + to_get + '.html'
    htmlfile = open(file_to_get, 'r')
    data = htmlfile.read()
    htmlfile.close()
    return data


# Styles and scripting for the page
main_page_head = get_template('head')

# The main page layout and title bar
main_page_content = get_template('content')

# A single movie entry html template
movie_tile_content = get_template('tile')

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
    
    
def get_moviedata(filename):
    movielist = []
    
    with open(filename, 'r') as csvfile:
        moviereader = csv.DictReader(csvfile)
        for movie in moviereader:
            movielist.append(media.Movie(title = movie['title'],
                                year = movie['year'],
                                poster_image_url = movie['poster_image_url'],
                                trailer_youtube_url = movie['trailer_youtube_url']))
    return movielist


def main():
    movies = get_moviedata('data/moviedata.csv')
    open_movies_page(movies)


if __name__ == '__main__':
    main()