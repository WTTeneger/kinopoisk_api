# Kinopoisk_films API

## content

0. [introduction](#introduction)
1. [Getting started](#Getting-started)
2. [Working with code](#Working-with-code)
3. [Description of functions](#Description-of-functions)
4. [Arguments](#Arguments)
    
## introduction
This API is used to get data from the kinopoisk website
____
[:arrow_up:content](#content)
___
## Getting started

### To work you will need the library
[Requests](https://pypi.org/project/requests/) 

### As well as the API key, which can be obtained on the site 
[kinopoiskapiunofficial](https://kinopoiskapiunofficial.tech/user)

### Install the Library
[filmapis](https://pypi.org/project/filmapis)
```
pip install filmapis
```

### Connecting the library
```py
import filmapis.filmapis as fa
```
____
[:arrow_up:content](#content)
____
## Working with code

### Creating an object is performed by passing the api key received from the site to the function 
[site](https://kinopoiskapiunofficial.tech/user)
```py
object_api = API_Cinema('API-KEY')
```
____
[:arrow_up:content](#content)
____
## Description of functions

#### Поиск по ключевому слову
```py
object_api.get_by_keyword(text)
```
____
#### Поиск по id на кинопоиске
```py
object_api.get_data_film(id_kinopoisk, append_to_response='RATING')
```
____
#### Берём скришоты из фильма
```py
object_api.get_frame_film(id_kinopoisk)
```
____
#### Берём видео связанные с фильма (трейлеры, вырезки)
```py
object_api.get_trailer_film(id_kinopoisk)
```
____
#### Берём сиквелы и приквелы фильма
```py
object_api.get_sequels_and_prequels_film(id_kinopoisk)
```
____
#### Берём все фильтры
```py
object_api.get_filters()
```
____
#### Берём фильмы по фильтру
```py
object_api.get_film_in_filters(counry=[], genre=[], order = 'RATING', types='ALL', ratingFrom=0, ratingTo=10, yearFrom=1888, yearTo=2021, page=1)
```
____
#### Берём фильмы по топу
```py
object_api.get_top_films(types='TOP_100_POPULAR_FILMS', page=1)
```
____
#### Берём похожие фильмы
```py
object_api.et_similars_film(id_kinopoisk)
```
____
#### Берём фильмы которые вышли по фильтру
```py
object_api.get_releaze_film(year = 2021, month = 'JANUARY', page=1)
```
____
#### Берём данные по студии которая снимала
```py
object_api.get_studios_date(id_kinopoisk)
```
____
#### Берём данные по студии которая снимала
```py
object_api.get_studios_date(id_kinopoisk)
```
____
### Films
#### Берём отзывы
```py
object_api.get_reviews(id_kinopoisk, page=1)
```
____
#### Берём подробный отзывы
```py
object_api.get_reviews_details(id_reviews)
```
____
### Staff
#### Берём всех кто работал над фильмом
```py
object_api.get_staff(id_kinopoisk)
```
____
#### Берём подробную информацию о работнике
```py
object_api.get_staff_details(id_person)
```
____









## Arguments
| Обозначение | Описание | Пример регулярного выражения|
|----:|:----:|:----------|
| literal | Строка содержит символьный литерал literal | foo |
| re1&#124;re2 | Строка содержит регулярные выражения `rel` или `re2` | foo&#124;bar |
