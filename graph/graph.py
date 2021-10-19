# Width search
# Graph implementation 
#                                                     page 146, chapter 6
#------------------------------------------------------------------------

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "chaire"]

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()          # creating a new queue
    search_queue += graph["you"]    # all neighbors are added to the list queue
    searched = []                   # array already for checked items

    while search_queue:

        person = search_queue.popleft()         # the first item is retrieved
        if not person in searched:
            if person_is_seller(person):
                
                print (person + "is a mango seller!")
                return True
            else:
                search_queue +=  graph[person]
                searched.append(person)         # adding to a checked array 
    return False
