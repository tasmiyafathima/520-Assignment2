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
                if score >= 90:
                    # distinction branch
                    passed.append((name, score, attendance, "Distinction"))
                elif score >= 70:
                    # merit branch
                    passed.append((name, score, attendance, "Merit"))
                else:
                    # pass branch
                    passed.append((name, score, attendance, "Pass"))
            else:
                continue
        else:
            continue
    passed.sort(key=lambda x: (-x[1], -x[2], x[0]))
    return [name for name, _, _, _ in passed]
