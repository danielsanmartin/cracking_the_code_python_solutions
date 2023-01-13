import pytest
from animal_shelter import *


@pytest.fixture
def animal_shelter():
    return AnimalShelter()


def test_enqueue(animal_shelter):
    animal_shelter.enqueue(Dog('Max'))
    animal_shelter.enqueue(Dog('Meggi'))
    animal_shelter.enqueue(Cat('Bob'))
    animal_shelter.enqueue(Cat('Kirk'))

    assert len(animal_shelter.cats) == 2
    assert len(animal_shelter.dogs) == 2


def test_dequeue_any_dog(animal_shelter):
    dog_1 = Dog('Max')
    dog_2 = Dog('Meggi')
    cat = Cat('Bob')
    animal_shelter.enqueue(dog_1)
    animal_shelter.enqueue(dog_2)
    animal_shelter.enqueue(cat)

    assert animal_shelter.dequeue_any() == dog_1


def test_dequeue_any_cat(animal_shelter):
    cat_1 = Cat('Sarah')
    dog_1 = Dog('Max')
    cat_2 = Cat('Bob')
    dog_2 = Dog('Meggi')

    animal_shelter.enqueue(cat_1)
    animal_shelter.enqueue(dog_1)
    animal_shelter.enqueue(cat_2)
    animal_shelter.enqueue(dog_2)

    assert animal_shelter.dequeue_any() == cat_1


def test_dequeue_dog(animal_shelter):
    dog_1 = Dog('Max')
    dog_2 = Dog('Meggi')
    cat_1 = Cat('Bob')
    animal_shelter.enqueue(dog_1)
    animal_shelter.enqueue(dog_2)
    animal_shelter.enqueue(cat_1)

    assert animal_shelter.dequeue_dog() == dog_1


def test_dequeue_cat(animal_shelter):
    dog_1 = Dog('Max')
    dog_2 = Dog('Meggi')
    cat_1 = Cat('Bob')
    animal_shelter.enqueue(dog_1)
    animal_shelter.enqueue(cat_1)
    animal_shelter.enqueue(dog_2)

    assert animal_shelter.dequeue_cat() == cat_1
