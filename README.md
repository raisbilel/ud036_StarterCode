# ud036_StarterCode
Source code for a Movie Trailer website.

# Usage
You should add your own movies to the file `mymovies.py` by instantiating an object of class `Movie()` and passing the following variables:

**movie_title** (str) : Contains the title of your newly added movie.
**poster_img_url** (str) : Contains the link to the poster image url of your newly added movie.
**trailer_url** (str) : Contains a youtube link to your movie's trailer.

Then, you should append your movie objects to the list `movies`.

Finally, you should execute the same file `mymovies.py` to generate your own movie trailer website. 

## Example :

This is how the file `mymovies.py` looks like initially

```
import media
import fresh_tomatoes

movies = []   # Initiates the movies containing list

# Define your movies here!


fresh_tomatoes.open_movies_page(movies)
```

I will add the **inception** movie to my library an example:

```
import media
import fresh_tomatoes

movies = []   # Initiates the movies containing list

# Define your movies here!
inception = media.Movie(
	'Inception',
	'https://i.ytimg.com/vi/E1iqGiX0lSg/movieposter.jpg',
	'https://www.youtube.com/watch?v=8hP9D6kZseM' )

movies.append(inception)  # Appends my new movie the movies list

fresh_tomatoes.open_movies_page(movies)
```
