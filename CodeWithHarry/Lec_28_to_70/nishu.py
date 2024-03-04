class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.attendance = {}

    def mark_attendance(self, status, date):
        if status.lower() == 'a' or status.lower() == 'p':
            self.attendance[date] = status.lower()

class AttendanceRegister:
    def __init__(self):
        self.date = None
        self.students = {}

    def set_date(self, date):
        self.date = date

    def add_student(self, student):
        self.students[student.roll_no] = student

    def mark_attendance(self, roll_no):
        if roll_no in self.students:
            student = self.students[roll_no]
            status = input(f"Mark attendance for {student.name} (a for Absent, p for Present): ")
            student.mark_attendance(status, self.date)
        else:
            print(f"Student with roll number {roll_no} not found.")

def generate_custom_students():
    student_names = [
        "Abhishek Kumar", "Dal Akib Salimbhai", "Alfiza Sandh", "Anas Mansuri", "Ayush Dabariya",
        "Bhumika Padia", "Darshan Jadav", "Manvar Dhavalkishorbhai", "Vekariya Flora Natvarlal",
        "Govind Kumar", "Harsh Devmurari", "Jeet Kumbhani", "Rathod Jiya Bharatbhai", "Kelvin Kava",
        "Keval Bhonkiya", "Krisha Makwana", "Manali Gohel", "Maulik Rohitbhai Dudhrejiya", "Mayank Gurnani",
        "Mayank Pravinchandra Chavda", "Mayank Rajeshbhai Thumar", "Moxa Hareshbhai Shah",
        "Naman Sureshbhai Vekariya", "Nancy Ketanbhai Suvagiya", "Nirbhay Hiteshbhai Thumar",
        "Satasiya Parv Atulbhai", "Prit Rathod", "Rishi Girishbhai Paghadar", "Sajjan Arvindbhai Pansuriya",
        "Sakhina Mohmadbhai Sandh", "Sanskriti Pinakin Trivedi", "Mansuri Shakil Asharaf Ali",
        "Viradiya Shlok Pankajbhai", "Shreyash Sharma", "Surbhi Chandreshbhai Sardhara",
        "Umang Sureshbhai Bhutani", "Vashi Bhatt", "Vishant Vipulbahi Radadiya", "Vraj Bavisa",
        "Vruta Bhatt", "Yogi Kshitijnath", "Slok Meena"
    ]
    
    students = [Student(i + 1, name) for i, name in enumerate(student_names)]
    return students

def main():
    date = input("Enter the date for attendance marking: ")
    attendance_register = AttendanceRegister()
    attendance_register.set_date(date)

    # Generate and add custom students to the register
    custom_students = generate_custom_students()
    for student in custom_students:
        attendance_register.add_student(student)

    for roll_no in sorted(attendance_register.students.keys()):
        student = attendance_register.students[roll_no]
        status = input(f"Mark attendance for {student.name} (a for Absent, p for Present): ")
        student.mark_attendance(status, date)

    print("\nAttendance Register:")
    for roll_no in sorted(attendance_register.students.keys()):
        student = attendance_register.students[roll_no]
        status = student.attendance.get(date, 'N/A')
        if status == 'a':
            status_display = 'Absent'
        elif status == 'p':
            status_display = 'Present'
        else:
            status_display = 'N/A'
        print(f"{student.name} (Roll No: {student.roll_no}): {status_display}")

if __name__ == "__main__":
    main()
