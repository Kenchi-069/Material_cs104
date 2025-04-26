store = []

with open("buggy_marksheet.txt", "r") as file:
    for line in file:
        store.append(line)

students = [x.strip().split(" ") for x in store]

sorted_students = sorted(students, key=lambda x: (x[0].split('_')[2], -int(x[1])))

print(sorted_students)