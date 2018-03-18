class Movie():
	"""Creates new Movie object. Requires passing a
	 movie title, poster iage, and a trailer url as 
	 parameters for initialisation"""

	# Defines the constructor function for Class Movie.
	def __init__(self,movie_title,poster_img_url,trailer_url):
		self.title = movie_title   
		self.poster_image_url = poster_img_url
		self.trailer_youtube_url = trailer_url

