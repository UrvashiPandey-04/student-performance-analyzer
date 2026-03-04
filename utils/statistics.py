def calculate_student_totals(data):
    """
    Adds total and average marks for each student
    """
    for student in data:
        total = student["Maths"] + student["Science"] + student["English"]
        average = total / 3

        student["Total"] = total
        student["Average"] = round(average, 2)

    return data


def class_average(data):
    """
    Calculates overall class average
    """
    total_sum = 0

    for student in data:
        total_sum += student["Average"]

    return round(total_sum / len(data), 2)


def find_topper(data):
    """
    Finds the student with highest average
    """
    topper = max(data, key=lambda student: student["Average"])
    return topper


def find_lowest(data):
    """
    Finds the student with lowest average
    """
    lowest = min(data, key=lambda student: student["Average"])
    return lowest


def subject_averages(data):
    """
    Calculates average marks for each subject
    """
    maths_total = 0
    science_total = 0
    english_total = 0

    for student in data:
        maths_total += student["Maths"]
        science_total += student["Science"]
        english_total += student["English"]

    total_students = len(data)

    return {
        "Maths": round(maths_total / total_students, 2),
        "Science": round(science_total / total_students, 2),
        "English": round(english_total / total_students, 2)
    }


def pass_percentage(data, passing_marks=40):
    """
    Calculates percentage of students passing
    """
    passed = 0

    for student in data:
        if (
            student["Maths"] >= passing_marks
            and student["Science"] >= passing_marks
            and student["English"] >= passing_marks
        ):
            passed += 1

    percentage = (passed / len(data)) * 100
    return round(percentage, 2)

def assign_grades(data):
    """
    Assign grades to students based on average marks
    """
    for student in data:
        avg = student["Average"]

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 40:
            grade = "D"
        else:
            grade = "F"

        student["Grade"] = grade

    return data


def student_ranking(data):
    """
    Sort students by average marks (highest first)
    """
    ranked_students = sorted(data, key=lambda student: student["Average"], reverse=True)
    return ranked_students


def top_students(data, n=5):
    """
    Return top N students
    """
    ranked = student_ranking(data)
    return ranked[:n]


def score_distribution(data):
    """
    Calculate performance distribution
    """
    distribution = {
        "90-100": 0,
        "80-89": 0,
        "70-79": 0,
        "60-69": 0,
        "50-59": 0,
        "Below 50": 0
    }

    for student in data:
        avg = student["Average"]

        if avg >= 90:
            distribution["90-100"] += 1
        elif avg >= 80:
            distribution["80-89"] += 1
        elif avg >= 70:
            distribution["70-79"] += 1
        elif avg >= 60:
            distribution["60-69"] += 1
        elif avg >= 50:
            distribution["50-59"] += 1
        else:
            distribution["Below 50"] += 1

    return distribution