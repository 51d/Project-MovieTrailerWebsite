import fresh_tomatoes
import media

# ALL MOVIE INSTANCES CONTAIN (title,storyline,box art,youtube trailer)
dangal = media.Movie('Dangal',
                     'Story of two sisters who learned wrestling'
                     'from their father and won a medal in commonwealth games',
                     'http://www.media.glamsham.com/download/poster'
                     '/images/dangal/04-Dangal.jpg',
                     'https://www.youtube.com/watch?v=x_7YlGv9u1g')

spiderman_homecoming = media.Movie('Spiderman homecoming',
                                   'SuperHero',
                                   'http://t0.gstatic.com/images?q=tbn:ANd9Gc'
                                   'T8W3Fe7DD101g0M7OCalJN9u675sQAJFslGCjvs7'
                                   '4PTOfEKt_t',
                                   'https://www.youtube.com/watch?v='
                                   'n9DwoQ7HWvI')

welcome = media.Movie('Welcome',
                      'A brother who is a underworld don want her'
                      'sister to marry a well stablised guy.',
                      'http://bharat-movies.com/hindi/img/MovieImg'
                      '/Welcome-2007-MovieImg.jpg',
                      'https://www.youtube.com/watch?v=QJCMdzuLG0I')

inception = media.Movie('Inception',
                        'A thief with the rare ability to enter'
                        'people\'s dreams.',
                        'http://t2.gstatic.com/images?q=tbn:ANd9GcRo9'
                        'vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD',
                        'https://www.youtube.com/watch?v=8hP9D6kZseM')

harry_potter = media.Movie('Harry Potter and the deathly hallows',
                           'Harry , Ron and Hermione begin a missi'
                           'on to destroy the Horcruxes',
                           'http://t3.gstatic.com/images?q=tbn:ANd9G'
                           'cTobkzVSJU5oZ9Pv_6bM0_o4RF_zFA9jyNwdHATG'
                           '90vKxyhOk5x',
                           'https://www.youtube.com/watch?v=_EC2tmFVNNE')

dawn_o_t_p_o_apes = media.Movie('Dawn of the Planet of the Apes',
                                'Caesor was offered protection of'
                                'his people and re-establishion of a '
                                'relationship with humans.',
                                'http://t1.gstatic.com/images?q=tbn:ANd'
                                '9GcRiFADcYKbJaffawZIolcpNA5aThmKHV'
                                'Ie3U8lnZCtsiqYyT51h',
                                'https://www.youtube.com/watch?v=3sHMCRaS3ao')

movie = [spiderman_homecoming, welcome, inception,
         harry_potter, dangal, dawn_o_t_p_o_apes]
# Movie list contains all out movie instances
# and passed to open_movies_page method.
fresh_tomatoes.open_movies_page(movie)

