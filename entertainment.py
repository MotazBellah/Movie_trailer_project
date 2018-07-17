import media
import fresh_tomatoes

interstaller = media.Movie("Interstaller", "Man search for a new planet",
                           "poster_image/interstaller.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "About escaping from prison",
                                   "poster_image/Shawshank.jpg",
                                   "https://www.youtube.com/" +
                                   "watch?v=6hB3S9bIaco")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/" +
                     "en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY&t=14s")

theory_of_everything = media.Movie("The theory of everything",
                                   "True story about Stephen Hawking",
                                   "poster_image/The_Theory_of_Everything.jpg",
                                   "https://www.youtube.com/" +
                                   "watch?v=Salz7uGp72c")

beautiful_mind = media.Movie("A beautiful mind", "True story about John Nash",
                             "poster_image/beautiful_mind.jpg",
                             "https://www.youtube.com/watch?v=WFJgUm7iOKw")

school_of_rock = media.Movie("School of Rock", "Using Rock music to learn",
                             "poster_image/school.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

movies = [interstaller, shawshank_redemption,
          avatar, theory_of_everything, beautiful_mind, school_of_rock]
fresh_tomatoes.open_movies_page(movies)
