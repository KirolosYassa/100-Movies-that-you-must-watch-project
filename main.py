import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

movies_list_descending = []
movies_list_ascending = []
movies_html_list = []
movies_html_list = soup.select("h3.title")
counter = 0
for movie in movies_html_list:
    try:
        movie_categorized = movie.get_text().split(")")
        movie_name = movie_categorized[1]
    except IndexError:
        movie_categorized = movie.get_text().split(":")
        movie_name = movie_categorized[1]
    finally:
        counter += 1
        # print(counter)
        # print(movie_name)
        movies_list_descending.append(movie_name)

print(movies_list_descending)

for i in range(len(movies_list_descending)-1, -1, -1):
    movies_list_ascending.append(movies_list_descending[i])
    
print(movies_list_ascending)
with open("movies_list_descending.txt", "w") as file:
    index = 1
    for movie in movies_list_ascending:
        file.write(f"{index}){movie}\n")
        index += 1
