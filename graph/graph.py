# Реализация графа 
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "chaire"]

def person_is_seller(name):
    return name[-1] == 'm'
def search(name):
    search_queue = deque()          # Создание новой очереди
    search_queue += graph["you"]    # Все соседи добавляются в очередь поиска
    searched = []

    while search_queue:

    person = search_queue.popleft()     # Извлекается первый элемент
    
    if not person in searched:

        if person_is_seller(person):
            print (person + "is a mango seller!")
            return True

    else:
        search_queue +=  graph[person]
        searched.append(person)

    return False

search(you)
