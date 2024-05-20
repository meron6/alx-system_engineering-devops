import requests
import sys
import csv

def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch employee details
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    
    # Fetch TODO list for the employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Extract employee username
    employee_name = employee_data.get('username')
    
    # Create CSV file name
    csv_file_name = f"{employee_id}.csv"
    
    # Write data to CSV
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, employee_name, task['completed'], task['title']])
    
    print(f"Data has been exported to {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
