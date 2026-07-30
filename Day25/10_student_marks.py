# Student Marks Summary

marks = {
    "Math": 90,
    "Python": 95,
    "OS": 88,
    "DSA": 91
}

grade = {
    subject: ("Pass" if mark >= 40 else "Fail")
    for subject, mark in marks.items()
}

print(grade)
