import time
import csv
import random
from student_management_system import StudentManagementSystem

def measure_time(func):
    """Decorator to measure function execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {(end - start)*1000:.2f} ms")
        return result
    return wrapper

class PerformanceTest:
    def __init__(self):
        self.sms = StudentManagementSystem()
        self.test_sizes = [100, 1000, 10000]
        self.sample_courses = ["Math", "Physics", "Chemistry", "Biology", "English"]

    def generate_student_data(self, n):
        """Generate n random student records."""
        students = []
        for i in range(n):
            student_id = f"{i:05d}"  # 5-digit ID
            name = f"Student_{i}"
            grades = {
                course: random.randint(60, 100)
                for course in self.sample_courses
            }
            students.append((student_id, name, grades))
        return students

    @measure_time
    def test_add_students(self, n):
        """Test adding n students."""
        students = self.generate_student_data(n)
        for student_id, name, grades in students:
            self.sms.add_student(student_id, name, grades)

    @measure_time
    def test_search_students(self, n):
        """Test searching for n random students."""
        for _ in range(n):
            student_id = f"{random.randint(0, n-1):05d}"
            self.sms.search_student(student_id)

    @measure_time
    def test_update_grades(self, n):
        """Test updating grades for n random students."""
        for _ in range(n):
            student_id = f"{random.randint(0, n-1):05d}"
            course = random.choice(self.sample_courses)
            new_grade = random.randint(60, 100)
            self.sms.update_grade(student_id, course, new_grade)

    @measure_time
    def test_calculate_gpas(self, n):
        """Test calculating GPAs for n random students."""
        for _ in range(n):
            student_id = f"{random.randint(0, n-1):05d}"
            self.sms.calculate_gpa(student_id)

    @measure_time
    def test_process_withdrawals(self, n):
        """Test processing withdrawals for n/10 random students."""
        for _ in range(n//10):  # Testing with 10% of total students
            student_id = f"{random.randint(0, n-1):05d}"
            self.sms.process_withdrawal(student_id)

    @measure_time
    def test_traverse_all(self):
        """Test traversing all students."""
        _ = self.sms.get_all_students()

    def run_all_tests(self):
        """Run all performance tests for different sizes."""
        print("\n🚀 Starting Performance Tests")
        print("=" * 50)

        for size in self.test_sizes:
            print(f"\n📊 Testing with {size} students:")
            print("-" * 50)
            
            # Reset SMS for each test size
            self.sms = StudentManagementSystem()
            
            # Run tests
            self.test_add_students(size)
            self.test_search_students(size)
            self.test_update_grades(size)
            self.test_calculate_gpas(size)
            self.test_process_withdrawals(size)
            self.test_traverse_all()

            # Memory usage (approximate)
            import sys
            memory_used = sys.getsizeof(self.sms.hash_table) + \
                         sum(sys.getsizeof(student) for student in self.sms.get_all_students())
            print(f"\nMemory Usage: {memory_used/1024:.2f} KB")
            print("=" * 50)

def generate_test_data(size):
    """Generate test data for students."""
    students = []
    courses = ['Math', 'Physics', 'Chemistry', 'Biology', 'Computer Science']
    
    for i in range(size):
        student_id = 1000 + i
        name = f"Student_{i}"
        grades = {course: random.randint(60, 100) for course in random.sample(courses, 3)}
        students.append((student_id, name, grades))
    
    return students

def run_performance_test(sizes=[100, 500, 1000, 5000, 10000]):
    """Run performance tests with different input sizes."""
    results = []
    
    for size in sizes:
        print(f"\nRunning tests with {size} students...")
        sms = StudentManagementSystem()
        test_data = generate_test_data(size)
        
        # Test 1: Adding students
        start_time = time.time()
        for student_id, name, grades in test_data:
            sms.add_student(student_id, name, grades)
        add_time = time.time() - start_time
        
        # Test 2: Searching for students (random sample of 100 searches)
        search_times = []
        for _ in range(100):
            random_id = random.choice(test_data)[0]
            start_time = time.time()
            sms.search_student(random_id)
            search_times.append(time.time() - start_time)
        avg_search_time = sum(search_times) / len(search_times)
        
        # Test 3: Updating grades (random sample of 100 updates)
        update_times = []
        for _ in range(100):
            random_id = random.choice(test_data)[0]
            start_time = time.time()
            sms.update_grade(random_id, "Math", random.randint(60, 100))
            update_times.append(time.time() - start_time)
        avg_update_time = sum(update_times) / len(update_times)
        
        # Test 4: Traversal time
        start_time = time.time()
        sms.get_all_students()
        traversal_time = time.time() - start_time
        
        # Test 5: Deletion (random sample of 100 deletions)
        delete_times = []
        delete_ids = random.sample([x[0] for x in test_data], 100)
        for del_id in delete_ids:
            start_time = time.time()
            sms.delete_student(del_id)
            delete_times.append(time.time() - start_time)
        avg_delete_time = sum(delete_times) / len(delete_times)
        
        results.append({
            'Input Size': size,
            'Add Time (s)': add_time,
            'Avg Search Time (s)': avg_search_time,
            'Avg Update Time (s)': avg_update_time,
            'Traversal Time (s)': traversal_time,
            'Avg Delete Time (s)': avg_delete_time,
            'Memory Usage (items)': sms.size
        })
    
    return results

def save_results_to_csv(results, filename='performance_results.csv'):
    """Save test results to a CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Input Size', 'Add Time (s)', 'Avg Search Time (s)', 
                     'Avg Update Time (s)', 'Traversal Time (s)', 
                     'Avg Delete Time (s)', 'Memory Usage (items)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    print(f"\nResults saved to {filename}")

def generate_operation_comparison_csv():
    """Generate CSV comparing operation times for different data structures."""
    operations = [
        ['Operation', 'Linked List', 'Hash Table', 'Combined Structure'],
        ['Search', 'O(n)', 'O(1)', 'O(1)'],
        ['Insert', 'O(1)*', 'O(1)', 'O(n)'],
        ['Delete', 'O(n)', 'O(1)', 'O(n)'],
        ['Traverse', 'O(n)', 'O(n)', 'O(n)'],
        ['Update', 'O(n)', 'O(1)', 'O(1)']
    ]
    
    with open('operation_comparison.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(operations)
    print("\nOperation comparison saved to operation_comparison.csv")

if __name__ == "__main__":
    # Run performance tests
    print("Starting performance tests...")
    results = run_performance_test()
    save_results_to_csv(results)
    
    # Generate operation comparison
    generate_operation_comparison_csv()

    # Run all performance tests for different sizes
    perf_test = PerformanceTest()
    perf_test.run_all_tests() 