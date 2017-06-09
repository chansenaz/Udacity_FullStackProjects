import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys who come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

stranger_than_fiction = media.Movie("Stranger Than Fiction",
                                    "Harold Crick begins hearing a disembodied voice narrating his life as it happens",
                                    "https://upload.wikimedia.org/wikipedia/en/f/ff/Stranger_Than_Fiction_%282006_movie_poster%29.jpg",
                                    "https://www.youtube.com/watch?v=PZpg8VII7es")

the_matrix = media.Movie("The Matrix",
                         "Follow the White Rabbit",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

mad_max = media.Movie("Mad Max: Fury Road",
                      "Max and Imperator Furiosa revolt against the tyrannical Immortan Joe",
                      "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8")

anchorman = media.Movie("Anchorman",
                        "Anchorman Ron Burgundy welcomes Veronica Corningstone into the male-dominated world of 1970s broadcast news",
                        "https://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg",
                        "https://www.youtube.com/watch?v=Ip6GolC7Mk0")

john_wick = media.Movie("John Wick",
                        "Legendary assassin John Wick (Keanu Reeves) un-retires",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
                        "https://www.youtube.com/watch?v=wDEWKx0PtUg")

hot_rod = media.Movie("Hot Rod",
                      "Rod Kimball attempts to perform one big stunt to save his step-father",
                      "https://upload.wikimedia.org/wikipedia/en/7/7f/Hot-rod-poster.jpg",
                      "https://www.youtube.com/watch?v=DhdrA9qz79o")

saving_private_ryan = media.Movie("Saving Private Ryan",
                                  "Captain John Miller takes his men behind enemy lines to find Private James Ryan",
                                  "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",
                                  "https://www.youtube.com/watch?v=zwhP5b4tD6g")

hot_fuzz = media.Movie("Hot Fuzz",
                       "Former London constable Nicholas Angel finds it difficult to adapt to his new assignment in the sleepy British village of Sandford",
                       "http://img.moviepostershop.com/hot-fuzz-movie-poster-2007-1020399805.jpg",
                       "https://www.youtube.com/watch?v=ayTnvVpj9t4")

movies = [hot_rod, john_wick, stranger_than_fiction, saving_private_ryan, toy_story, hot_fuzz,
          the_matrix, mad_max,  anchorman, avatar]

fresh_tomatoes.open_movies_page(movies)
