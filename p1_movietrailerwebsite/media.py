import webbrowser


class Movie:
    def __init__(self, title, year, poster_image_url, trailer_youtube_url):
        self.title = title
        self.year = year
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
