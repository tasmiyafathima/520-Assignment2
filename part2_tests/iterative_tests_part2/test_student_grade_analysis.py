# Auto-generated pytest tests for student_grade_analysis
import importlib
mod = importlib.import_module('part2_tests.programs')
from part2_tests.programs.student_grade_analysis import student_grade_analysis



# ************** Iteration-0 ******************
def test_student_grade_analysis_1():
    # Single student passing simplest condition (score>=50, attendance>=75)
    students = [("Alice", 55, 80)]
    assert student_grade_analysis(students) == ["Alice"]


def test_student_grade_analysis_2():
    # Another student hitting the same branch as test_student_grade_analysis_1
    # Score >=50, attendance >=75, Pass branch
    students = [("David", 60, 80)]
    assert student_grade_analysis(students) == ["David"]



# ************** Iteration-1 ******************

def test_student_grade_analysis_3():
    # Student fails due to low attendance
    # Does not touch Pass/Distinction/Merit branches
    students = [("Bob", 60, 70)]  # score >=50, attendance <75
    assert student_grade_analysis(students) == []

def test_student_grade_analysis_4():
    # Another student failing due to low attendance
    # Only exercises the same branch as test_student_grade_analysis_2
    students = [("Charlie", 65, 70)]  # score >=50, attendance <75
    assert student_grade_analysis(students) == []



# ************** Iteration-2 ******************


def test_student_grade_analysis_5():
    # Student fails due to low score
    students = [("Bob", 40, 80)]
    assert student_grade_analysis(students) == []

def test_student_grade_analysis_6():
    # Student fails due to low attendance
    students = [("Charlie", 60, 70)]
    assert student_grade_analysis(students) == []


# ************** Iteration-3 ******************


def test_student_grade_analysis_7():
    # Distinction branch (score>=90)
    students = [("Dave", 95, 80)]
    assert student_grade_analysis(students) == ["Dave"]


def test_student_grade_analysis_8():
    # Multiple students, tie-breaking by score and attendance
    students = [
        ("Alice", 95, 90),
        ("Bob", 95, 85),
        ("Charlie", 85, 95),
        ("Dave", 85, 95),
        ("Eve", 60, 80)
    ]
    # Sorted by score desc, then attendance desc, then name asc
    assert student_grade_analysis(students) == ["Alice","Bob","Charlie","Dave","Eve"]

