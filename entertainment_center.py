#Author: Paramdeep Singh
# Project Name: Movie Trailer Website

#import media.py file and fresh_tomatoes.py file
import media, fresh_tomatoes

#First Movie details
venom = media.Movie("Venom",
"One of Marvel's most enigmatic, complex and badass characters comes to the big screen, starring Academy Award® nominated actor Tom Hardy as the lethal protector Venom.",
"https://m.media-amazon.com/images/M/MV5BNzAwNzUzNjY4MV5BMl5BanBnXkFtZTgwMTQ5MzM0NjM@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://www.youtube.com/watch?v=xLCn88bfW1o")

#Second Movie Details
central_intelligence = media.Movie("Central Intelligence",
"Central Intelligence is a 2016 American action comedy film directed by Rawson Marshall Thurber, and written by Thurber, Ike Barinholtz and David Stassen. The film stars Kevin Hart and Dwayne Johnson as two old high school friends who go on the run after one of them joins the CIA in order to save the world from a terrorist who has an intention to sell satellite codes.",
"https://images-na.ssl-images-amazon.com/images/I/81ioA49NNgL._SY550_.jpg",
"https://www.youtube.com/watch?v=MxEw3elSJ8M")

#Third Movie Details
spectre = media.Movie("Spectre", "The latest James Bond movie", "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",
"https://www.youtube.com/watch?v=vBnGxAkdh_k")

#Fourth Movie Details
matrix = media.Movie("The Matrix","The world is a simulation", "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
"https://www.youtube.com/watch?v=vKQi3bBA1y8")

#Fifth Movie Details
martian = media.Movie("The Martian","A man is stuck on Mars",
"https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg","https://www.youtube.com/watch?v=lQqhfq87FgY")

#Sixth Movie Details
resident_evil = media.Movie("Resident Evil","Zombie-causing virus escapes from the lab","https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg",
"https://www.youtube.com/watch?v=u6uDnd_v5Bw")
                         
                   



#creating array of all movies details
movies = [venom, central_intelligence, spectre, matrix, martian, resident_evil]

#passing the movies array data to function declared in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)