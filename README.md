# Kinopoisk_films API

## content

0. [introduction](#introduction)
1. [Getting started](#Getting-started)
2. [Working with code](#Working-with-code)
3. [Description of functions](#Description-of-functions)
    
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

### Films
#### Search by keyword
```py
object_api.get_by_keyword(text)
```
____
#### Search by id on kinopoisk
```py
object_api.get_data_film(id_kinopoisk, append_to_response='RATING')
```
____
#### We take screenshots from the movie
```py
object_api.get_frame_film(id_kinopoisk)
```
____
#### We take videos related to the film (trailers, clippings)
```py
object_api.get_trailer_film(id_kinopoisk)
```
____
#### We take the sequels and prequels of the film
```py
object_api.get_sequels_and_prequels_film(id_kinopoisk)
```
____
#### We take all the filters
```py
object_api.get_filters()
```
____
#### We take movies by filter
```py
object_api.get_film_in_filters(counry=[], genre=[], order = 'RATING', types='ALL', ratingFrom=0, ratingTo=10, yearFrom=1888, yearTo=2021, page=1)
```
____
#### We take films by the top
```py
object_api.get_top_films(types='TOP_100_POPULAR_FILMS', page=1)
```
____
#### We take similar movies
```py
object_api.et_similars_film(id_kinopoisk)
```
____
#### We take the films that were released by the filter
```py
object_api.get_releaze_film(year = 2021, month = 'JANUARY', page=1)
```
____
#### We take data on the studio that was shooting
```py
object_api.get_studios_date(id_kinopoisk)
```
### reviews
#### We take reviews
```py
object_api.get_reviews(id_kinopoisk, page=1)
```
____
#### We take detailed reviews
```py
object_api.get_reviews_details(id_reviews)
```
### Staff
#### We take everyone who worked on the film
```py
object_api.get_staff(id_kinopoisk)
```
____
#### erem detailed information about the employee
```py
object_api.get_staff_details(id_person)
```
[:arrow_up:content](#content)
