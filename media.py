#import webbrowser module
import webbrowser

#defining class Movie
class Movie():
    def __init__(self, movie_title, movie_description, poster_img, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_description
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube