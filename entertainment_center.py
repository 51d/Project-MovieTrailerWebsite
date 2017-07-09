import fresh_tomatoes
import media

# ALL MOVIE INSTANCES CONTAIN (title,storyline,box art,youtube trailer)
dangal = media.Movie('Dangal',
                     'Story of two sisters who learned wrestling from their father and won a medal in commonwealth games',
                     'http://www.media.glamsham.com/download/poster/images/dangal/04-Dangal.jpg',
                     'https://www.youtube.com/watch?v=x_7YlGv9u1g')

spiderman_homecoming = media.Movie('Spiderman homecoming',
                                   'SuperHero',
                                   'http://images.complex.com/complex/images/c_fill,g_center,w_1200/fl_lossy,pg_1,q_auto/uc7ae2rek8ne8ov0ue8e/spider-man-homecoming-poster',
                                   'https://www.youtube.com/watch?v=n9DwoQ7HWvI')

welcome = media.Movie('Welcome',
                      'A comedy film in which a brother who is a underworld don want her sister to marry a well stablised guy.',
                      'http://bharat-movies.com/hindi/img/MovieImg/Welcome-2007-MovieImg.jpg',
                      'https://www.youtube.com/watch?v=QJCMdzuLG0I')

inception = media.Movie('Inception',
                        'A thief with the rare ability to enter people\'s dreams and steal their secrets from their subconscious.',
                        'http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD',
                        'https://www.youtube.com/watch?v=8hP9D6kZseM')

harry_potter = media.Movie('Harry Potter and the deathly hallows',
                           'Harry , Ron and Hermione begin a mission to destroy the Horcruxes, the sources of Voldemort\'s immortality.',
                           'http://t3.gstatic.com/images?q=tbn:ANd9GcTobkzVSJU5oZ9Pv_6bM0_o4RF_zFA9jyNwdHATG90vKxyhOk5x',
                           'https://www.youtube.com/watch?v=_EC2tmFVNNE')

dawn_o_t_p_o_apes = media.Movie('Dawn of the Planet of the Apes',
                                'a small band of human forces Caesar (leader of apes family) to grapple with the dual challenge of protecting his people and re-establishing a relationship with the remaining human population -- the latter being Caesar\'s secret wish.',
                                'http://t1.gstatic.com/images?q=tbn:ANd9GcRiFADcYKbJaffawZIolcpNA5aThmKHVIe3U8lnZCtsiqYyT51h',
                                'https://www.youtube.com/watch?v=3sHMCRaS3ao')

movie = [spiderman_homecoming, welcome, inception, harry_potter, dangal, dawn_o_t_p_o_apes]
fresh_tomatoes.open_movies_page(movie)
