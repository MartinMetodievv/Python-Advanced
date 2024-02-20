number_of_students = int(input())

students = {}

for _ in range(number_of_students):
    name, grade = input().split()
    if name not in students.keys():
        students[name] = []
    students[name].append(float(grade))
for key_name, value_grade in students.items():
    avg_grade = f'{sum(value_grade) / len(value_grade):.2f}'
    form_grades = ' '.join([f"{x:.2f}" for x in value_grade])
    print(f"{key_name} -> {form_grades} (avg: {avg_grade})")
# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00
