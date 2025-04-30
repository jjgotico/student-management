# Student Management System

A Python-based Student Management System that implements both Hash Tables and Linked Lists for efficient student record management.

## Features

- **Fast Student Lookup**: O(1) time complexity using hash table
- **Ordered Student Records**: Maintained using linked list
- **Grade Management**: Add and update student grades
- **GPA Calculation**: Supports both numeric and letter grades
- **Administrative Tools**: Process withdrawals and notifications

## Data Structures

The system uses two primary data structures:
1. **Hash Table**: For O(1) lookups by student ID
2. **Linked List**: For maintaining insertion order and sequential access

## Core Functions

```python
# Student Management
add_student(student_id, name, grades=None)
delete_student(student_id)
search_student(student_id)

# Academic Records
update_grade(student_id, course, grade)
calculate_gpa(student_id)

# Administrative
process_withdrawal(student_id)
notify_professors(student_id)
update_financial_aid(student_id)

# Data Access
get_all_students()
print_student_details(student_id)
print_all_students()
```

## Usage Example

```python
# Create a new student management system
sms = StudentManagementSystem()

# Add a student
sms.add_student("001", "John Doe", {"Math": 90, "Physics": 85})

# Update a grade
sms.update_grade("001", "Math", 95)

# Calculate GPA
gpa = sms.calculate_gpa("001")
```

## Implementation Details

- Student records are stored in both a hash table and a linked list
- Hash table provides O(1) access by student ID
- Linked list maintains insertion order and enables sequential access
- Grade calculations support both numeric (0-100) and letter grades (A+ to F)

## Requirements

- Python 3.x
- No additional dependencies required

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Navigate to the project directory:
```bash
cd student-management-system
```

3. Run the example:
```bash
python student_management_system.py
```
