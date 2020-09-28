#!/usr/bin/env python

__author__ = 'r-bolling with help from Kenzie Academy Lessons'

import requests

def get_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    r = r.json()
    print(
        f'There are {r["number"]} astronaut(s) in space'
    )
    for i in range(0, r["number"]):
        print(
            f'Name: {r["people"][i]["name"]}, '
            f'Craft: {r["people"][i]["craft"]}'
        )
    return r

def get_space_coords():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    return r.json()

def main():
    get_astronauts()
    coords = get_space_coords()
    pass


if __name__ == '__main__':
    main()
