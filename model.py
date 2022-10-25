import random
from typing import Dict, List

NUM_STUDENTS = 10
NUM_SCHOOLS = 3

school_indices = list(range(NUM_SCHOOLS))

class School:
    def __init__(self, capacity: int, i: int) -> None:
        self.capacity = capacity
        self.students = []
        self.i = i

    def is_full(self) -> bool:
        return self.capacity == len(self.students)

    def add_student(self, student: int) -> None:
        self.students.append(student)

    def display(self):
        print(f'School {self.i}')
        print('--------')
        for el in self.students:
            print(el)
        print('')

class Student:
    def __init__(self, i: int) -> None:
        self.i = i + 1 # student index 
        self.preferences = random.sample(school_indices, k=len(school_indices)) #randomizes a student's preference over schools
        self.priority = self.generate_priority() # randomizes a student's priority at all schools
        self.assigned = False

    def __str__(self):
        return f'Student {self.i} -- Preferences: {self.preferences} -- Priorities: {self.priority}'

    def generate_priority(self) -> Dict[int, int]:
        """
        Generates a student's priority at all schools.
        Goes by the following assumptions: 
        - All students live within walking distance of a school (i.e. have some priority somewhere).
        - They have a 25% chance to have a sibling. If they have a sibling they will be assigned to a random school.
        - They have a 25% chance of living in a walk zone to some school.
        """
        has_sibling = random.randrange(4) == 1
        in_walkzone = random.randrange(4) == 1

        priorities = {s: 0 for s in school_indices}
        if has_sibling == True:
            # +2 to a random school's priority
            priorities[random.randrange(NUM_SCHOOLS)] += 2
        if in_walkzone == True:
            # +1 to a random school's priority -- can be the same as above
            priorities[random.randrange(NUM_SCHOOLS)] += 1
        return priorities

def generate_students() -> List[Student]:
    return [Student(i) for i in range(NUM_STUDENTS)]

def divide(lst: List, min_size: int, split_size: int) -> List[List]:
    # from https://stackoverflow.com/questions/14427531/how-to-split-a-list-into-n-random-but-min-sized-chunks
    it = iter(lst)
    from itertools import islice
    size = len(lst)
    for i in range(split_size - 1,0,-1):
        s = random.randint(min_size, size -  min_size * i)
        yield list(islice(it,0,s))
        size -= s
    yield list(it)

def generate_schools() -> List[School]:
    chunks = divide(range(NUM_STUDENTS), min_size=2, split_size=NUM_SCHOOLS)
    print(chunks)
    capacities = [len(el) for el in chunks]
    return [School(i, c) for c, i in enumerate(capacities)]