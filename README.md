python-fastest-route
====================

Python script to determine the fastest airfare route for a set of cities and the costs to fly between them.

Premise
-------

Given an associative array of different cities and the flight costs to travel between them, find the cheapest way to visit each city, under the following restrictions:

 - Avoid local cycles, or paths shorter than each connected city
 - Your trip must start in the first city
 - You must visit each city only once

Usage
-----

    python airfare.py

Time 
----

This script currently takes roughly 20 minutes to run on my Mid-2009 MacBook Pro with 4GB of RAM.

Printing each individual step to the command-line slows down the process immensely, while also having the effect on my machine of causing an error since my MacBook Pro eventually runs out of SWOP memory.

Customization
-------------

The python 'route' object in the script is a dictionary which can easily be changed to suit whichever array of cities/costs you may have.

To allow the route to start in any city, make the first city in the route dictionary a "bogus" city with the ability to travel to each of the "real" cities at a cost of 0. This will simulate starting at any city.