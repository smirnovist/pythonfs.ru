#!/usr/bin/env python3

from pprint import pprint
from dictionaries_2_data import data

movies = {}
years = {}
directors = {}
actors = {}


def organize_data():
    for i in data:
        movies[i['movie']] = {
            'year': i['year'],
            'director': i['director'],
            'starring': i['starring'],
        }
        if i['year'] not in years:
            years[i['year']] = {}
        years[i['year']][i['movie']] = movies[i['movie']]
        if i['director'] not in directors:
            directors[i['director']] = {}
        directors[i['director']][i['movie']] = movies[i['movie']]
        for j in i['starring']:
            if j not in actors:
                actors[j] = {}
            actors[j][i['movie']] = movies[i['movie']]


def find_data_by_actor(actor):
    career = []
    for i, k in actors['Джейсон Стэйтем'].items():
        a = k['starring'].copy()
        del a[k['starring'].index('Джейсон Стэйтем')]
        career.append({'movie': i, 'year': k['year'], 'director': k['director'], 'starring_with': a})
    return career


organize_data()

print('movies = ')
pprint(movies)
print('years = ')
pprint(years)
print('directors = ')
pprint(directors)
print('actors = ')
pprint(actors)
'Джейсон Стэйтем'


come = find_data_by_actor('Джейсон Стэйтем')
pprint(come)

print('movies = ')
pprint(movies)