import webbrowser
class Video():
    def __init__(self, title, storyline):
        self.title = title
        self.storyline = storyline

class Movie(Video):
    def __init__(self, title, storyline, poster_img, trailer):
        Video.__init__(self, title, storyline)
        self.poster_img = poster_img
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
