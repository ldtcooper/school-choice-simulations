import random
from model import Student, School, NUM_STUDENTS, school_indices

students = [Student(i) for i in range(NUM_STUDENTS)]
assigned_students = []
schools = [School(3, 0), School(3, 1), School(4, 2)]

def priority_sort(a: Student, b: Student, k: int) -> int:
    if a.priority[k] > b.priority[k]:
        return 1
    elif a.priority[k] < b.priority[k]:
        return -1
    else:
        return random.choice([-1,1]) # randomly generate break for tie

## ALGORITHM ##
for k in school_indices: # goes through all n choices in order -- number of ranked schools same as number of schools
    for s in schools:
        if s.is_full():
            continue

        eligible_students =  [t for t in students if t.priorities[k] == s.i] # students with school s as kth choice
        eligible_students.sort(key=lambda x: x.priority[k]) #sort students by priority for k
        
        for el in eligible_students:
        
