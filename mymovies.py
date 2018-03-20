import media
import fresh_tomatoes

movies = []   # Initiates the movies containing list

inception = media.Movie(
	'Inception',
	'https://i.ytimg.com/vi/E1iqGiX0lSg/movieposter.jpg',
	'https://www.youtube.com/watch?v=8hP9D6kZseM' )
movies.append(inception)  # Appends my new movie the movies list

catch = media.Movie(
	'Catch Me If You Can',
	'https://images-na.ssl-images-amazon.com/images/I/51bPnAto--L.jpg',
	'https://www.youtube.com/watch?v=SosRcIMCr5g')
movies.append(catch)  # Appends my new movie the movies list

fresh_tomatoes.open_movies_page(movies)