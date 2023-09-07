# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked list data structure.

from collections import deque
class animal_shelter:
    def __init__(self):
        self.dogq = deque()
        self.catq = deque()
        self.time = 0

    def enqueue(self, type: int):        #Dog: 0; Cat: 1
        if type == 0:
            self.dogq.append(self.time)
        else:
            self.catq.append(self.time)
        self.time += 1

    def dequeue_dog(self):       #Dog: 0; Cat: 1; Oldest: 3
        if len(self.dogq) > 0:
           self.dogq.popleft()
    
    def dequeue_cat(self):
        if len(self.catq) > 0:
            self.catq.popleft()
    
    def dequeue_any(self):
        dog = self.dogq[0]
        cat = self.catq[0]
        if dog<cat:
            self.dogq.popleft()
        else:
            self.catq.popleft()