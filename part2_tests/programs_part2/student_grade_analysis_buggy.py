# part2_tests/programs/student_grade_analysis.py

def student_grade_analysis(students):
    """
    students: list of tuples (name:str, score:int, attendance:int)
    
    Returns a sorted list of names of students who pass:
    - score >= 50
    - attendance >= 75
    Sorted by score descending, then attendance descending, then name ascending.
    """
    passed = []
    for name, score, attendance in students:
        if score >= 50:
            if attendance >= 75:
                if score > 90: # bug introduced
                    # distinction branch
                    passed.append((name, score, attendance, "Distinction"))
                elif score > 70: # bug introduced
                    # merit branch
                    passed.append((name, score, attendance, "Merit"))
                else:
                    # pass branch
                    passed.append((name, score, attendance, "Pass"))
            else:
                # insufficient attendance branch
                continue
        else:
            # failed score branch
            continue

    # Sorting by score desc, attendance desc, name asc
    passed.sort(key=lambda x: (-x[1], -x[2], x[0]))
    # Return only names
    return [name for name, _, _, _ in passed]
