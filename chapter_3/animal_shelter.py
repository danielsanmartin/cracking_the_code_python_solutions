# 3.6
# Page 239
# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linkedlist data structure.
from collections import deque


class Animal:

    def __init__(self, name):
        self.name = name
        self.order = 0

    def is_older_than(self, animal):
        return self.order < animal.order

    def __str__(self):
        return self.name


class Dog(Animal):
    def __init__(self, n):
        super().__init__(n)


class Cat(Animal):
    def __init__(self, n):
        super().__init__(n)


class AnimalShelter:

    def __init__(self):
        self.cats = deque()
        self.dogs = deque()
        self.order = 0

    def enqueue(self, animal):
        animal.order = self.order

        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)
        else:
            raise Exception("Animal not allowed!")
        self.order += 1

    def dequeue_any(self) -> Animal:
        if len(self.dogs) == 0:
            return self.cats.popleft()
        elif len(self.cats) == 0:
            return self.dogs.popleft()
        elif len(self.dogs) == 0 and len(self.cats) == 0:
            raise IndexError('No animals.')

        first_dog = self.dogs[0]
        first_cat = self.cats[0]

        if first_cat.is_older_than(first_dog):
            return self.cats.popleft()
        else:
            return self.dogs.popleft()

    def dequeue_dog(self) -> Dog:
        if len(self.dogs) != 0:
            return self.dogs.popleft()
        else:
            raise IndexError('No dogs.')

    def dequeue_cat(self) -> Cat:
        if len(self.cats) != 0:
            return self.cats.popleft()
        else:
            raise IndexError('No cats.')
