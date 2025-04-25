import time
import csv
import random
from student_management_system import StudentManagementSystem

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