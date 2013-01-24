import datetime
import gc

# speeds up process by turning off garbage collection
gc.disable()

# dictionary of airfare route costs
routes = {
  1: {
    2: 940,
    3: 720,
    4: 600,
    5: 720,
    6: 850,
    7: 800,
    8: 670,
    9: 610,
    10: 770,
    15: 1220
  },
  2: {
    3: 390,
    4: 640,
    5: 450,
    6: 340,
    10: 590,
    13: 1100
  },
  3: {
    2: 390,
    4: 470,
    5: 270,
    9: 510,
    10: 420,
    12: 730,
    15: 540
  },
  4: {
    2: 640,
    3: 470,
    5: 440,
    6: 610,
    7: 800,
    8: 490,
    9: 640,
    10: 420,
    12: 630,
    15: 910
  },
  5: {
    2: 450,
    3: 270,
    4: 440,
    6: 350,
    7: 560,
    8: 320,
    10: 500,
    13: 850,
    15: 825
  },
  6: {
    2: 340,
    4: 610,
    5: 350,
    7: 760,
    8: 470,
    9: 470,
    10: 520,
    12: 480,
    15: 870
  },
  7: {
    4: 800,
    5: 560,
    6: 760,
    10: 360,
    13: 970,
    14: 870
  },
  8: {
    4: 490,
    5: 320,
    6: 470,
    10: 310,
    12: 580,
    13: 940
  },
  9: {
    3: 510,
    4: 640,
    6: 470,
    10: 640,
    11: 910,
    12: 630,
    13: 830,
    14: 750
  },
  10: {
    2: 590,
    3: 420,
    4: 420,
    5: 500,
    6: 520,
    7: 360,
    8: 310,
    9: 640,
    11: 850,
    12: 910,
    13: 750,
    14: 610,
    15: 735
  },
  11: {
    9: 910,
    10: 850,
    12: 620,
    13: 880,
    14: 600
  },
  12: {
    3: 730,
    4: 630,
    6: 480,
    8: 580,
    9: 630,
    10: 910,
    11: 620,
    13: 420,
    14: 350
  },
  13: {
    2: 1100,
    5: 850,
    7: 970,
    8: 940,
    9: 830,
    10: 750,
    11: 880,
    12: 420,
    14: 400,
    15: 285
  },
  14: {
    7: 870,
    9: 750,
    10: 610,
    11: 600,
    12: 350,
    13: 400,
    15: 375
  },
  15: {
    3: 540,
    4: 910,
    5: 825,
    6: 870,
    10: 735,
    13: 285,
    14: 375
  }
}

# function to determine the cheapest route
def find_cheapest_route(route=[1], cost=0):
    # display to terminal where the program is at; uncomment the next line to track progress (slows down process significantly)
    # print route
    
    # if route is complete, return the results
    if len(route) == 15:
        return cost, route

    # set initial variables
    cheapest_cost = None
    fastest_route = route

    # otherwise, evaluate possible children routes
    for a,b in routes[route[-1]].iteritems():
        # only evaluate next step if not already in route
        if a not in route:
            # recursive call
            new_cost, new_route = find_cheapest_route(route=(route + [a]), cost=(cost + b))
            
            # test to see if it's a cheaper route than other routes found
            if new_cost and (not cheapest_cost or new_cost < cheapest_cost):
                # assign cheapest cost and fastest route
                cheapest_cost = new_cost
                fastest_route = new_route
    
    # return the cheapest route found
    return cheapest_cost, fastest_route

# main function
def main():
    print 'Starting to process the best airfare route...'
    
    start_time = datetime.datetime.now() # start time 
    cost, route = find_cheapest_route() # evaluate routes
    end_time = datetime.datetime.now() - start_time # calculate endtime
    
    # display results
    print 'Cheapest Airfare Cost: %s\nRoute Taken: %s\n Time spent computing this result: %s' % (cost, route, end_time)

# run program
if __name__ == "__main__":
    main()