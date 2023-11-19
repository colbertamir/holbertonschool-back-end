#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Checking the command-line arguments
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    # Parsing the employee ID from command line argument
    employee_id = int(sys.argv[1])
    
    # URLs for fetching user and to-do data based on employee ID
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        # Fetching user data from API
        response = requests.get(url)
        response.raise_for_status()
        user_data = response.json()

        # Fetching to-do list for the user
        response = requests.get(todo_url)
        response.raise_for_status()
        todos = response.json()

        # Extracting finished tasks and calculating total and finished tasks count
        completed_tasks = [task['title'] for task in todos if task['completed']]
        total_tasks = len(todos)
        num_completed_tasks = len(completed_tasks)

        # Displaying user's task completion status and finalized tasks
        print(f"Employee {user_data['name']} is done with tasks"
              f" ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task}")

    except requests.exceptions.RequestException as e:
        # Handling request-related exceptions
        print(f"Error occurred: {e}")
