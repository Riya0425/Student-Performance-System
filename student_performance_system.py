# ------------------ DATA ------------------
students = [
    {"name": "Aarav", "math": 78, "science": 72, "english": 75},
    {"name": "Diya", "math": 85, "science": 80, "english": 82},
    {"name": "Karan", "math": 62, "science": 65, "english": 60},
    {"name": "Meera", "math": 90, "science": 92, "english": 88},
    {"name": "Rohan", "math": 55, "science": 58, "english": 54}
]

# ------------------ FUNCTIONS ------------------
def calculate_total_and_average(student):
    total = student["math"] + student["science"] + student["english"]
    avg = total / 3
    return total, avg


def calculate_class_data():
    total_avg_sum = 0
    pass_count = 0
    fail_count = 0

    for student in students:
        _, avg = calculate_total_and_average(student)
        total_avg_sum += avg
        if avg >= 60:
            pass_count += 1
        else:
            fail_count += 1

    class_avg = total_avg_sum / len(students)
    return class_avg, pass_count, fail_count


def calculate_topper_lowest():
    topper_name = ""
    topper_avg = -1
    lowest_name = ""
    lowest_avg = 101

    for student in students:
        _, avg = calculate_total_and_average(student)
        if avg > topper_avg:
            topper_avg = avg
            topper_name = student["name"]
        if avg < lowest_avg:
            lowest_avg = avg
            lowest_name = student["name"]

    return topper_name, topper_avg, lowest_name, lowest_avg


def calculate_subject_analysis():
    math_total = science_total = english_total = 0

    for student in students:
        math_total += student["math"]
        science_total += student["science"]
        english_total += student["english"]

    count = len(students)
    math_avg = math_total / count
    science_avg = science_total / count
    english_avg = english_total / count

    strongest_subject = "Math"
    strongest_avg = math_avg
    weakest_subject = "Math"
    weakest_avg = math_avg

    if science_avg > strongest_avg:
        strongest_avg = science_avg
        strongest_subject = "Science"
    if science_avg < weakest_avg:
        weakest_avg = science_avg
        weakest_subject = "Science"
    if english_avg > strongest_avg:
        strongest_avg = english_avg
        strongest_subject = "English"
    if english_avg < weakest_avg:
        weakest_avg = english_avg
        weakest_subject = "English"

    return math_avg, science_avg, english_avg, strongest_subject, weakest_subject


def show_all_students():
    for student in students:
        _, avg = calculate_total_and_average(student)
        result = "Pass" if avg >= 60 else "Fail"
        print(student["name"], "Average:", avg, "Result:", result)


def show_class_summary():
    class_avg, passed, failed = calculate_class_data()
    print("Class Average:", class_avg)
    print("Passed:", passed)
    print("Failed:", failed)


def show_topper_lowest():
    topper, topper_avg, lowest, lowest_avg = calculate_topper_lowest()
    print("Topper:", topper, "Average:", topper_avg)
    print("Lowest Performer:", lowest, "Average:", lowest_avg)


def show_subject_analysis():
    math_avg, science_avg, english_avg, strongest, weakest = calculate_subject_analysis()
    print("Math Average:", math_avg)
    print("Science Average:", science_avg)
    print("English Average:", english_avg)
    print("Strongest Subject:", strongest)
    print("Weakest Subject:", weakest)


def show_ranking():
    student_averages = []
    for student in students:
        _, avg = calculate_total_and_average(student)
        student_averages.append([student["name"], avg])

    for i in range(len(student_averages)):
        for j in range(i + 1, len(student_averages)):
            if student_averages[j][1] > student_averages[i][1]:
                student_averages[i], student_averages[j] = student_averages[j], student_averages[i]

    rank = 1
    for s in student_averages:
        print("Rank", rank, ":", s[0], "Average:", s[1])
        rank += 1


# ------------------ MENU ------------------
while True:
    print("\n------ MENU ------")
    print("1. Show all students")
    print("2. Show class summary")
    print("3. Show topper & lowest performer")
    print("4. Show subject analysis")
    print("5. Show ranking")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        show_all_students()
    elif choice == "2":
        show_class_summary()
    elif choice == "3":
        show_topper_lowest()
    elif choice == "4":
        show_subject_analysis()
    elif choice == "5":
        show_ranking()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
