import requests
import expanddouban
import bs4
import csv
import copy

"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
	url += "," + category
	url += "," + location
	return url

class Movie:
	def __init__(self, name = "No Name", rate = -1.0, location = "", category = "", info_link = "", cover_link = ""):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link
		self.cover_link = cover_link

	def allInfo(self):
		return [self.name, self.rate, self.location, self.category, self.info_link, self.cover_link]

"""
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):
	movie_list = []
	url = getMovieUrl(category, location)
	html = expanddouban.getHtml(url, True)
	soup = bs4.BeautifulSoup(html, "lxml")
	movie_div = soup.find(class_="list-wp").find_all("a", recursive=False)
	for item in movie_div:
		movie_list.append(Movie(item.find(class_="title").string, item.find(class_="rate").string, location, category, item.get("href"), item.find(class_="pic").img.get("src")))
	return movie_list

def max3(d):
	count_ranking = sorted(d.items(), key=lambda item:item[1], reverse=True)
	return list(zip(*count_ranking[:3]))


cat_list = ["剧情", "喜剧", "动作"]
loc_list = ["中国大陆", "美国", "香港", "台湾", "日本", "韩国", "英国", "法国", "德国", "意大利", "西班牙", "印度", "泰国", "俄罗斯", "伊朗", "加拿大", "澳大利亚", "爱尔兰", "瑞典", "巴西", "丹麦"]

# with open('movies.csv','w') as f:
# 	f_csv = csv.writer(f)
# 	for category in cat_list:
# 		for location in loc_list:
# 			movie_list = getMovies(category, location)
# 			for item in movie_list:
# 				f_csv.writerow(item.allInfo())

with open('movies.csv', 'r') as f:
	reader = csv.reader(f)
	highScoredMovies = list(reader)

loc_dict = dict(zip(loc_list, loc_list))
for key in loc_dict:
	loc_dict[key] = 0
movie_dict = dict(zip(cat_list, cat_list))
for key in movie_dict:
	movie_dict[key] = copy.deepcopy(loc_dict)

for item in highScoredMovies:
	movie_dict[item[3]][item[2]]+= 1

with open('output.txt', 'w') as f:
	for key in movie_dict:
		total = 0
		for i in movie_dict[key]:
			total += movie_dict[key][i]
		ranking = max3(movie_dict[key])
		percentage = list(ranking[1])
		for i in range(len(ranking[1])):
			percentage[i] = str(round(ranking[1][i]/total*100, 2)) + "%"
		f.write(key + "分类中数量前三名的地区是：" + "，".join(ranking[0]) + "，占该分类电影总数的百分比分别为：" + "，".join(percentage) + "。\n")





