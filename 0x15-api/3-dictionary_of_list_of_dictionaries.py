mport json
import requests

def fetch_data(url):
    response = requests.get(url)
    return response.json()

def main():
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch users and todos data
    users = fetch_data(users_url)
    todos = fetch_data(todos_url)

    # Create a dictionary to store all tasks by user
    all_tasks = {}

    # Map user IDs to usernames
    user_dict = {user['id']: user['username'] for user in users}

    # Iterate over all tasks and structure them in the required format
    for task in todos:
        user_id = task['userId']
        if user_id not in all_tasks:
            all_tasks[user_id] = []
        
        task_info = {
            "username": user_dict[user_id],
            "task": task['title'],
            "completed": task['completed']
        }
        all_tasks[user_id].append(task_info)
    
    # Write the structured data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=4)

if __name__ == "__main__":
    main()
