class Student:
    def __init__(self, student_id, name, grades=None):
        self.student_id = student_id
        self.name = name
        self.grades = grades if grades else {}
        self.courses = []
        self.next = None  # for linked list implementation

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

class StudentNode:
    def __init__(self, student):
        self.student = student
        self.next = None

class StudentManagementSystem:
    def __init__(self):
        self.head = None  # for linked list
        self.hash_table = {}  # for O(1) lookups by ID
        self.size = 0

    def add_student(self, student_id, name, grades=None):
        """Add a new student to both linked list and hash table."""
        if student_id in self.hash_table:
            print(f"Student with ID {student_id} already exists!")
            return False

        new_student = Student(student_id, name, grades)
        new_node = StudentNode(new_student)

        # Add to linked list
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        # Add to hash table
        self.hash_table[student_id] = new_student
        self.size += 1
        return True

    def delete_student(self, student_id):
        """Delete a student from both data structures."""
        if student_id not in self.hash_table:
            print(f"Student with ID {student_id} not found!")
            return False

        # Remove from hash table
        del self.hash_table[student_id]

        # Remove from linked list
        if not self.head:
            return False

        if self.head.student.student_id == student_id:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next:
            if current.next.student.student_id == student_id:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next

        return False

    def search_student(self, student_id):
        """Search for a student by ID using hash table for O(1) lookup."""
        return self.hash_table.get(student_id)

    def update_grade(self, student_id, course, grade):
        """Update a student's grade for a specific course."""
        student = self.search_student(student_id)
        if student:
            student.grades[course] = grade
            return True
        return False

    def get_all_students(self):
        """Return all students in the system using linked list traversal."""
        students = []
        current = self.head
        while current:
            students.append(current.student)
            current = current.next
        return students

    def print_student_details(self, student_id):
        """Print detailed information about a specific student."""
        student = self.search_student(student_id)
        if student:
            print(f"\nStudent ID: {student.student_id}")
            print(f"Name: {student.name}")
            print("Grades:")
            for course, grade in student.grades.items():
                print(f"  {course}: {grade}")
        else:
            print(f"Student with ID {student_id} not found!")

    def print_all_students(self):
        """Print all students in the system."""
        if not self.head:
            print("No students in the system.")
            return

        print("\nAll Students:")
        print("-" * 50)
        current = self.head
        while current:
            student = current.student
            print(f"ID: {student.student_id}, Name: {student.name}")
            if student.grades:
                print("Grades:", end=" ")
                for course, grade in student.grades.items():
                    print(f"{course}: {grade}", end=" | ")
                print()
            print("-" * 50)
            current = current.next

    def notify_professors(self, student_id):
        """Notify professors when a student withdraws."""
        student = self.search_student(student_id)
        if student:
            for course in student.courses:
                print(f"Notification: Student {student.name} withdrawn from {course}")

    def update_financial_aid(self, student_id):
        """Update financial aid status."""
        student = self.search_student(student_id)
        if student:
            print(f"Financial aid updated for student: {student.name}")

    def process_withdrawal(self, student_id):
        """Process complete student withdrawal."""
        student = self.search_student(student_id)
        if student:
            self.notify_professors(student_id)
            self.update_financial_aid(student_id)
            self.delete_student(student_id)
            return True
        return False

    def calculate_gpa(self, student_id):
        """
        Calculate a student's GPA based on their grades.
        Returns float value on 4.0 scale.
        """
        student = self.search_student(student_id)
        if not student or not student.grades:
            return 0.0
        
        # Grade to GPA point conversion
        grade_points = {
            'A+': 4.0, 'A': 4.0, 'A-': 3.7,
            'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D+': 1.3, 'D': 1.0, 'F': 0.0
        }
        
        # For numerical grades (assuming 100-point scale)
        def convert_numeric_to_gpa(grade):
            if grade >= 93: return 4.0    # A
            elif grade >= 90: return 3.7   # A-
            elif grade >= 87: return 3.3   # B+
            elif grade >= 83: return 3.0   # B
            elif grade >= 80: return 2.7   # B-
            elif grade >= 77: return 2.3   # C+
            elif grade >= 73: return 2.0   # C
            elif grade >= 70: return 1.7   # C-
            elif grade >= 67: return 1.3   # D+
            elif grade >= 63: return 1.0   # D
            else: return 0.0              # F

        total_points = 0
        total_courses = len(student.grades)
        
        for course, grade in student.grades.items():
            if isinstance(grade, str):
                # Letter grade
                total_points += grade_points.get(grade.upper(), 0.0)
            else:
                # Numeric grade
                total_points += convert_numeric_to_gpa(grade)
        
        return round(total_points / total_courses, 2) if total_courses > 0 else 0.0

# Example usage and testing
if __name__ == "__main__":
    # Create a new student management system
    sms = StudentManagementSystem()

    # Add some students
    sms.add_student(1001, "John Doe", {"Math": 85, "Physics": 90})
    sms.add_student(1002, "Jane Smith", {"Math": 95, "Physics": 88})
    sms.add_student(1003, "Bob Johnson", {"Math": 78, "Physics": 85})

    # Print all students
    print("\nInitial Student List:")
    sms.print_all_students()

    # Search for a student
    print("\nSearching for student 1002:")
    sms.print_student_details(1002)

    # Update a grade
    sms.update_grade(1001, "Math", 88)
    print("\nAfter updating John's Math grade:")
    sms.print_student_details(1001)

    # Delete a student
    sms.delete_student(1002)
    print("\nAfter deleting Jane Smith:")
    sms.print_all_students()

    # Try to search for deleted student
    print("\nTrying to find deleted student (1002):")
    sms.print_student_details(1002)

    print("\nThe future of student management...")
    print("- Real-time grade updates")
    print("- Instant academic record access")
    print("- Seamless enrollment management")
    print("- Scalable to any institution size")
    print("- All possible with our hybrid system")

