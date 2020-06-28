from dijkstra_node import *

if __name__=="__main__":
    kolkata = City("Kolkata")
    bangalore = City("Bangalore")
    gangtok = City("Gangtok")
    delhi = City("Delhi")
    mumbai = City("Mumbai")
    chennai = City("Chennai")
    hyderabad = City("Hyderabad")

    kolkata.add_route(bangalore,4000)
    kolkata.add_route(delhi,3500)
    kolkata.add_route(mumbai,3500)
    kolkata.add_route(hyderabad,3700)
    kolkata.add_route(gangtok,5000)
    bangalore.add_route(delhi,6000)
    bangalore.add_route(mumbai,2800)
    bangalore.add_route(chennai,2000)
    bangalore.add_route(hyderabad,2100)
    mumbai.add_route(bangalore,2600)
    mumbai.add_route(delhi,2800)
    delhi.add_route(kolkata,3400)
    delhi.add_route(mumbai,2700)
    delhi.add_route(gangtok,7000)
    chennai.add_route(bangalore,2500)
    chennai.add_route(hyderabad,2600)
    hyderabad.add_route(bangalore,2400)
    hyderabad.add_route(chennai,2300)
    gangtok.add_route(kolkata,5600)


    #kolkata.print_routes()


    def dijkstra(starting_city,other_cities):
        routes_from_city = {} #Format: {Kolkata:[0,None],Bangalore:[4000,Kolkata]}
        routes_from_city[starting_city] = [0,starting_city]
        #[0,Kolkata]
        for city in other_cities:
            routes_from_city[city] = [float('inf'),None]
            #Setting all cities to [infinite,<city name>]
        
        visited_cities = []
        current_city = starting_city
        #current_city = Kolkata

        while current_city:
            visited_cities.append(current_city)
            #visited_cities = [Kolkata]
            for city,price in current_city.routes.items(): #city,price = bangalore,4000
                if routes_from_city[city][0] > price + routes_from_city[current_city][0]:
                    #routes_from_city[bangalore][0] == infinite > 4000 + 0;
                    routes_from_city[city] = [price+routes_from_city[current_city][0],current_city]
                    #routes_from_city[bangalore] = 4000+0, Kolkata
        
            current_city = None
            cheapest_route_from_current_city = float('inf')

            for city,price in routes_from_city.items():
                #bangalore,4000
                if (price[0]<cheapest_route_from_current_city) and (city not in visited_cities):
                    cheapest_route_from_current_city = price[0]
                    current_city = city

        return routes_from_city


    routes = dijkstra(bangalore,[kolkata,delhi,mumbai,gangtok])
    for city,price in routes.items():
        print(city.name,"->",price[0])