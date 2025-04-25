class Student:
    def __init__(self, student_id, name, grades=None):
        self.student_id = student_id
        self.name = name
        self.grades = grades if grades else {}
        self.next = None  # for linked list implementation

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