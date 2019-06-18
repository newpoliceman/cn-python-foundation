import requests
import expanddouban
import bs4

"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
    url += "," + category
    url += "," + location
    return url

class Movie:
	def __init__(self, name = "No Name", rate = 0.0, location = "", category = "", info_link = "", cover_link = ""):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link

"""
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):
	movie_list = []
	url = getMovieUrl(category, location)
	html = expanddouban.getHtml(url, True)
	soup = bs4.BeautifulSoup(html, "html.parser")
	movie_div = soup.find(class_="list-wp").find_all("a", recursive=False)
	for item in movie_div:
		movie_list.append(Movie(item.find(class_="title").string, item.find(class_="rate").string, location, category, item.get("href"), item.find(class_="pic").img.get("src")))
	return movie_list

print(len(getMovies("剧情", "韩国")))
