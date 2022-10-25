from model import school_indices, generate_students, generate_schools

students = generate_students()
schools = generate_schools()

## ALGORITHM ##
for k in school_indices: # goes through all n choices in order -- number of ranked schools same as number of schools
    for s in schools:
        print(s.i)
        if s.is_full():
            continue # go to next school if full

        eligible_students = [t for t in students if ((t.preferences[k] == s.i) and not t.assigned)] # students with school s as kth choice
        eligible_students.sort(key=lambda x: x.priority[k]) #sort students by priority for k
        
        for el in eligible_students:
            s.add_student(el)
            el.assigned = True
            print(f'Student {el.i} to school {s.i}')
            if s.is_full():
                break # break out of assignment and into next s-loop if school fills up

for s in schools:
    s.display()
