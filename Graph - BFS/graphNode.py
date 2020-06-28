class Person:
    name = ""
    visited = False
    friends = []

    def __init__(self,name,friends=[]):
        self.name = name
        self.friends = friends

    def add_friend(self,friend):
        self.friends.append(friend)

    
    def getAllConnections(self):
        reset_list = [self]
        queue = [self]
        self.visited = True
        while queue != []:
            current_vertex = queue.pop(0)
            print(current_vertex.name)

            for friend in current_vertex.friends:
                if not friend.visited:
                    reset_list.append(friend)
                    queue.append(friend)
                    friend.visited = True

        for node in reset_list:
            node.visited = False



    