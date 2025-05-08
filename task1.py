record = {
  "Alice": 85
}

name = input("Enter the student's name: ")
try:
  print(f"{name}'s marks: {record[name]}")
except KeyError:
  print("Student not found")