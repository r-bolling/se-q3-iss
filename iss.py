#!/usr/bin/env python

__author__ = '''r-bolling with help from Kenzie Academy Lessons
open-notify documentation
http://open-notify.org/Open-Notify-API/ISS-Pass-Times/
'''

import requests
import time
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

def world_map(coords, indy):
    iss_location = coords['iss_position']
    indy_time = indy[0]
    indy_coords = indy[1]
    screen = Screen()
    screen.setworldcoordinates(-180, -180, 180, 180)
    screen.addshape('iss.gif')
    screen.setup(720, 360)
    screen.bgpic('map.gif')
    iss = Turtle()
    iss.pencolor('yellow')
    iss.shape('iss.gif')
    iss.penup()
    iss.goto(indy_coords['lon'], indy_coords['lat'])
    iss.pendown()
    iss.dot(5, 'yellow')
    iss.write(indy_time)
    iss.penup()
    iss.goto(float(iss_location['longitude']), float(iss_location['latitude']))
    screen.exitonclick()
    pass

def iss_indianapolis():
    payload = {'lat': 39.7684, 'lon': -86.1581}
    r = requests.get('http://api.open-notify.org/iss-pass.json', params=payload)
    r = r.json()
    first_pass = r['response'][0]['risetime']
    first_pass = time.ctime(first_pass)
    return first_pass, payload

def main():
    get_astronauts()
    coords = get_space_coords()
    indy_pass = iss_indianapolis()
    world_map(coords, indy_pass)
    pass


if __name__ == '__main__':
    main()
