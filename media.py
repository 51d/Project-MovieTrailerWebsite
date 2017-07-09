import webbrowser
# creating a class movie to store all related data 
# of a movie that we wish to display.

class Movie:

    def __init__(self, m_title, m_storyline, m_poster, youtube_trailer):
        # the __init__ method is called when an instance is declared
        # and here contains all properties of the movie.
        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = m_poster
        self.trailer_youtube_url = youtube_trailer
    
    def trailer(self):
        # method trailer displays the movie trailer video from youtube.
        webbrowser.open('self.trailer_youtube_url')
