from utils.statistics import (
    calculate_student_totals,
    class_average,
    find_topper,
    find_lowest,
    subject_averages,
    pass_percentage,
    assign_grades,
    student_ranking,
    top_students,
    score_distribution
)


def generate_report(data):

    # Calculate totals and averages
    data = calculate_student_totals(data)

    # Assign grades
    data = assign_grades(data)

    total_students = len(data)

    avg_class = class_average(data)

    topper = find_topper(data)

    lowest = find_lowest(data)

    subjects = subject_averages(data)

    pass_percent = pass_percentage(data)

    ranked = student_ranking(data)

    top5 = top_students(data)

    distribution = score_distribution(data)

    print("\n📊 CLASS PERFORMANCE REPORT\n")

    print("Total Students:", total_students)
    print("Class Average:", avg_class)

    print("\n🏆 Topper:", topper["Name"], "(", topper["Average"], ")")
    print("📉 Lowest Performer:", lowest["Name"], "(", lowest["Average"], ")")

    print("\n📚 Subject Averages")
    print("Maths:", subjects["Maths"])
    print("Science:", subjects["Science"])
    print("English:", subjects["English"])

    print("\n✅ Pass Percentage:", pass_percent, "%")

    print("\n🏅 Top 5 Students")
    for i, student in enumerate(top5, start=1):
        print(i, ".", student["Name"], "-", student["Average"], "Grade:", student["Grade"])

    print("\n📊 Score Distribution")
    for category, count in distribution.items():
        print(category, ":", count, "students")