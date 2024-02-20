def students_credits(*args):
    courses = {}
    final = 0
    message = ''
    for x in args:
        course, credit, max_points, diyan_points = x.split("-")
        test_percent = (int(diyan_points) / int(max_points)) * 100
        course_credit = int(credit) * (test_percent / 100)
        final += course_credit
        courses[course] = course_credit
    if final >= 240:
        message += f"Diyan gets a diploma with {final:.1f} credits.\n"
    else:
        difference = 240 - final
        message += f"Diyan needs {difference:.1f} credits more for a diploma.\n"
    sorted_courses = dict(sorted(courses.items(), key=lambda x: -x[1]))
    for k, v in sorted_courses.items():
        message += f'{k} - {v:.1f}\n'
    return message


print(students_credits("Computer Science-12-300-250", "Basic Algebra-15-400-200", "Algorithms-25-500-490"))
