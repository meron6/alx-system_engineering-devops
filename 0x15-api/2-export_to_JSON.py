import requests
import sys
import json

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
    
    # Create JSON file name
    json_file_name = f"{employee_id}.json"
    
    # Prepare data for JSON
    tasks = []
    for task in todos_data:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        }
        tasks.append(task_data)
    
    data = {str(employee_id): tasks}
    
    # Write data to JSON file
    with open(json_file_name, 'w') as json_file:
        json.dump(data, json_file)
    
    print(f"Data has been exported to {json_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
