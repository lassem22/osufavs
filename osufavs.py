import re
import requests
from bs4 import BeautifulSoup
from collections import Counter

def getfavmaps(id):
  maplist = []
  page = requests.get("https://old.ppy.sh/pages/include/profile-beatmaps.php?u="+ id +"&m=0")
  soup = BeautifulSoup(page.content, 'html.parser')
  fav = soup.find(id="beatmapsFavourite")
  fav_items = fav.find_all(class_="prof-beatmap")
  for beatmap in fav_items :
    maplist.append(beatmap.get('id')[4:])

  return maplist

def getfavmappers(id):
  mapperlist = []
  page = requests.get("https://old.ppy.sh/pages/include/profile-beatmaps.php?u="+ id +"&m=0")
  soup = BeautifulSoup(page.content, 'html.parser')
  fav = soup.find(id="beatmapsFavourite")
  fav_items = fav.find_all(class_="prof-beatmap")
  for beatmap in fav_items :
    bs = beatmap.find_all('b')
    mapper = bs[1].find('a')
    mapperlist.append(mapper.get('href')[3:])

  return mapperlist


#set userids here
u1_id = "896613"
u2_id = "918297"

u1_maps = getfavmaps(u1_id)
u2_maps = getfavmaps(u2_id)

u1_mappers = getfavmappers(u1_id)
u2_mappers = getfavmappers(u2_id)

shared_maps = list(set(u1_maps) & set(u2_maps))
shared_mappers = list(set(u1_mappers) & set(u2_mappers))

print("Shared Maps:")
print(shared_maps)
print("")

print("")
print("Shared Mappers:")
print(shared_mappers)
print("")

print("")
print("Mapper Occurrence:")
print("")
print("User 1:")
print(Counter(u1_mappers))
print("")
print("User 2:")
print(Counter(u2_mappers))


