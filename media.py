import webbrowser


class Movie():
    def __init__(self,movie_title,movie_poster,movie_storyline,trailer_youtube):
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
