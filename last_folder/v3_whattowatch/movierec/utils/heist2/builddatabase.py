import json
from movierec.models import Movie, Genre, Person, Language, Keyword
import tmdbsimple as tmdb

tmdb.API_KEY = "f2eee9cde7536b5ef17767e4e9a97239"

def populateNetflix():
	i = 0

	while i < 16:
		print "Netflix page: " + str(i)
		fo = open('netflix/netflix_'+str(i)+'.json', 'r')
		json_list = json.load(fo)
		for result in json_list['results']:
			if result['themoviedb'] == 0 or result['imdb'] is None or result['poster_400x570'] == 'http://static-api.guidebox.com/misc/default_movie_400x570.jpg':
				continue

			e = Movie.objects.filter(identifier=int(result['id']))

			if len(e):
				m = Movie(identifier=result['id'],
                          themoviedb=result['themoviedb'],
                          imdb=result['imdb'],
                          rating=result['rating'],
                          rottentomatoes=result['rottentomatoes'],
                          metacritic=result['metacritic'],
                          common_sense_media=result['common_sense_media'],
                          poster=result['poster_400x570'],
                          title=result['title'],
                          date=result['release_year'],
                          netflix_available=True))
				m.save()
			else:
				obj = Movie.objects.get(identifier=int(result['id']))
				obj.netflix_available = True
				obj.save()
		i += 1
	print "Done populating Netflix"


def populateAmazon():
	i = 0

	while i < 52:
		print "Amazon page: " + str(i)
		fo = open('amazon/amazon_'+str(i)+'.json', 'r')
		json_list = json.load(fo)
		for result in json_list['results']:
			if result['themoviedb'] == 0 or result['imdb'] is None or result['poster_400x570'] == 'http://static-api.guidebox.com/misc/default_movie_400x570.jpg':
				continue

			e = Movie.objects.filter(identifier=int(result['id']))

			if len(e):
				m = Movie(identifier=result['id'],
                          themoviedb=result['themoviedb'],
                          imdb=result['imdb'],
                          rating=result['rating'],
                          rottentomatoes=result['rottentomatoes'],
                          metacritic=result['metacritic'],
                          common_sense_media=result['common_sense_media'],
                          poster=result['poster_400x570'],
                          title=result['title'],
                          date=result['release_year'],
                          amazon_available=True))
				m.save()
			else:
				obj = Movie.objects.get(identifier=int(result['id']))
				obj.amazon_available = True
				obj.save()
		i += 1
	print "Done populating Amazon"


def populateHulu():
	i = 0

	while i < 5:
		print "Hulu page: " + str(i)
		fo = open('hulu/hulu_'+str(i)+'.json', 'r')
		json_list = json.load(fo)
		for result in json_list['results']:
			if result['themoviedb'] == 0 or result['imdb'] is None or result['poster_400x570'] == 'http://static-api.guidebox.com/misc/default_movie_400x570.jpg':
				continue

			e = Movie.objects.filter(identifier=int(result['id']))

			if len(e):
				m = Movie(identifier=result['id'],
                          themoviedb=result['themoviedb'],
                          imdb=result['imdb'],
                          rating=result['rating'],
                          rottentomatoes=result['rottentomatoes'],
                          metacritic=result['metacritic'],
                          common_sense_media=result['common_sense_media'],
                          poster=result['poster_400x570'],
                          title=result['title'],
                          date=result['release_year'],
                          hulu_available=True))
				m.save()
			else:
				obj = Movie.objects.get(identifier=int(result['id']))
				obj.hulu_available = True
				obj.save()
		i += 1
	print "Done populating Hulu"


def populateHbo():
	i = 0

	while i < 5:
		print "HBO page: " + str(i)
		fo = open('hbo/hbo_'+str(i)+'.json', 'r')
		json_list = json.load(fo)
		for result in json_list['results']:
			if result['themoviedb'] == 0 or result['imdb'] is None or result['poster_400x570'] == 'http://static-api.guidebox.com/misc/default_movie_400x570.jpg':
				continue

			e = Movie.objects.filter(identifier=int(result['id']))

			if len(e):
				m = Movie(identifier=result['id'],
                          themoviedb=result['themoviedb'],
                          imdb=result['imdb'],
                          rating=result['rating'],
                          rottentomatoes=result['rottentomatoes'],
                          metacritic=result['metacritic'],
                          common_sense_media=result['common_sense_media'],
                          poster=result['poster_400x570'],
                          title=result['title'],
                          date=result['release_year'],
                          hbo_available=True))
				m.save()
			else:
				obj = Movie.objects.get(identifier=int(result['id']))
				obj.hbo_available = True
				obj.save()
		i += 1
	print "Done populating HBO"


def getManualLinks():
	with open("netflix_links.txt", "r") as file:
		for line in file:
			array = line.split(" ")
			id = int(array[0])
			netflix_link = array[1]
			m = Movie.objects.filter(identifier=id)[:1]
			if len(m) != 0:
				movie = m[0]
				if len(netflix_link) == 0:
					movie.netflix_available = False
				else:
					movie.netflix = netflix_link
				movie.save()
	with open("amazon_links.txt", "r") as file:
		for line in file:
			array = line.split(" ")
			id = int(array[0])
			amazon_link = array[1]
			m = Movie.objects.filter(identifier=id)[:1]
			if len(m) != 0:
				movie = m[0]
				if len(amazon_link) == 0:
					movie.amazon_available = False
				else:
					movie.amazon = amazon_link
				movie.save()
	with open("hulu_links.txt", "r") as file:
		for line in file:
			array = line.split(" ")
			id = int(array[0])
			hulu_link = array[1]
			m = Movie.objects.filter(identifier=id)[:1]
			if len(m) != 0:
				movie = m[0]
				if len(hulu_link) == 0:
					movie.hulu_available = False
				else:
					movie.hulu = hulu_link
				movie.save()
	with open("hbo_links.txt", "r") as file:
		for line in file:
			array = line.split(" ")
			id = int(array[0])
			hbo_link = array[1]
			m = Movie.objects.filter(identifier=id)[:1]
			if len(m) != 0:
				movie = m[0]
				if len(hbo_link) == 0:
					movie.hbo_available = False
				else:
					movie.hbo = hbo_link
				movie.save()

populateNetflix()
populateAmazon()
populateHulu()
populateHbo()
