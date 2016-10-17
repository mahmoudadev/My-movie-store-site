import media
import fresh_tomatoes



toy_story = media.Movie("TOY STROY","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "A toy came into life",
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')


hobit = media.Movie("The Hobit",
                    "https://upload.wikimedia.org/wikipedia/en/a/a9/The_Hobbit_trilogy_dvd_cover.jpg",
                    "A small man make a journey",
                    "https://www.youtube.com/watch?v=nOGsB9dORBg")


harry_potter = media.Movie("Harry Potter and the Sorcerer's Stone",
                           "http://static.rogerebert.com/uploads/movie/movie_poster/harry-potter-and-the-sorcerers-stone-2001/large_uLGaJ9FgPWf7EUgwjp9RTmHemw8.jpg",
                           "A child entered into a magic school",
                           "https://www.youtube.com/watch?v=VyHV0BRtdxo")


inception = media.Movie("Inception 2008",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
                        
                        "incept an idea on someone's head",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")


the_shawshank = media.Movie("The Shawshank Redemption (1994)",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
                            "A perisoner try to escape from his jail ",
                            "https://www.youtube.com/watch?v=6hB3S9bIaco")

limitless = media.Movie("Limitless",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcQSJVRsIEFYFBlTfJAygejBNdbFFlvOEShCKNeeYMSEqwyFtyW0",
                        "one drag changes life",
                        "https://www.youtube.com/watch?v=jOLqNOfzus4")

me_before_you = media.Movie("Me Before You (2016)",
                            "http://t3.gstatic.com/images?q=tbn:ANd9GcR-Pi0mGMztx_eCHb3f7BrSiL0Gy_YfMk0Ef6WUSPx2KZ135n-a",
                            "ffff",
                            "https://www.youtube.com/watch?v=Eh993__rOxA")

movies =[toy_story,hobit,harry_potter,inception,the_shawshank,limitless,me_before_you]

fresh_tomatoes.open_movies_page(movies)





