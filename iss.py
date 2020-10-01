#!/usr/bin/env python

__author__ = 'r-bolling with help from Kenzie Academy Lessons'

import requests
from turtle import Screen, Turtle

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

def world_map(coords):
    iss_location = coords['iss_position']
    screen = Screen()
    screen.setworldcoordinates(-360, -180, 360, 180)
    screen.addshape('iss.gif')
    screen.setup(720, 360)
    screen.bgpic('map.gif')
    iss = Turtle()
    iss.shape('iss.gif')
    iss.penup()
    iss.goto(float(iss_location['longitude']), float(iss_location['latitude']))
    screen.exitonclick()
    pass

def main():
    get_astronauts()
    coords = get_space_coords()
    world_map(coords)
    pass


if __name__ == '__main__':
    main()
