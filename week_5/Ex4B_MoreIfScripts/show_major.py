student_name  = "Will Poindexter"
student_major = "CSCI"

major_lookup = {
    "BIOL": ("Biology",          "Science Bldg, Room 310"),
    "CSCI": ("Computer Science", "Sheppard Hall, Room 314"),
    "ENG":  ("English",          "Kerr Hall, Room 201"),
    "HIST": ("History",          "Kerr Hall, Room 114"),
    "MKT":  ("Marketing",        "Westly Hall, Room 310"),
}

if student_major in major_lookup:
    major_name, office = major_lookup[student_major]
else:
    major_name = "<unknown>"
    office     = ""

print(f"Student: {student_name}")
print(f"Major: {major_name}")
if office:
    print(f"Department Office: {office}")