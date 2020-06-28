class City:
    def __init__(self,name,routes={}):
        self.name = name
        self.routes = routes

    def add_route(self,city,price):
        self.routes[city] = price

    def print_routes(self):
        if self.routes == {}:
            print("No routes found")
        else:
            for city_name in self.routes:
                print(city_name.name,"->",self.routes[city_name])

    def dijkstra(self,starting_city,other_cities):
        routes_from_city = {} #Format: {Kolkata:[0,None],Bangalore:[4000,Kolkata]}
        routes_from_city[starting_city] = [0,starting_city]
        
        for city in other_cities:
            routes_from_city[city] = [float('inf'),None]
        
        visited_cities = []
        current_city = starting_city

        while current_city:
            visited_cities.append(current_city)
            for city,price in current_city.routes:
                if routes_from_city[city][0] > price + routes_from_city[current_city][0]:
                    routes_from_city[city] = [price+routes_from_city[current_city][0],current_city]

            current_city = None
            cheapest_route_from_current_city = float('inf')

            for city,price in routes_from_city:
                if (price[0]<cheapest_route_from_current_city) and (city not in visited_cities):
                    cheapest_route_from_current_city = price[0]
                    current_city = city

        return routes_from_city