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
| tile | Description | Call example|
|----:|:----:|:----------|
| literal | Строка содержит символьный литерал literal | foo |
| re1&#124;re2 | Строка содержит регулярные выражения `rel` или `re2` | foo&#124;bar |
| поиск по ключевуму слову | Принимает ввденённый текст и ищет совпадения | ```py get_by_keyword(text)``` |



## Arguments
| Обозначение | Описание | Пример регулярного выражения|
|----:|:----:|:----------|
| literal | Строка содержит символьный литерал literal | foo |
| re1&#124;re2 | Строка содержит регулярные выражения `rel` или `re2` | foo&#124;bar |
