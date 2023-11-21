#!/usr/bin/python3
"""Gather data from an API & export task info to CSV"""

import csv
import json
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    """Check for correct # of arg and their format"""
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    """Extract the employee ID from the command-line argument"""
    employee_id = int(sys.argv[1])

    """URLs for fetching user & to-do data based on the employee ID"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = ("https://jsonplaceholder.typicode.com/"
                f"todos?userId={employee_id}")

    try:
        """Fetch user data from the API"""
        with urllib.request.urlopen(user_url) as response:
            user_data = json.loads(response.read().decode())

        """Grabs to-do list for the user"""
        with urllib.request.urlopen(todo_url) as response:
            todos = json.loads(response.read().decode())

        """Extract completed tasks and format the task info"""
        completed_tasks = [
            (str(employee_id),
             user_data['username'],
             str(task['completed']),
             task['title'])
            for task in todos
        ]

        """Create a CSV file and write task info to it"""
        filename = f"{employee_id}.csv"
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            csvwriter.writerows(completed_tasks)

        """Print confirmation message after writing task data to CSV"""
        print(f"Task data for employee {user_data['username']} written to {filename}")

    except urllib.error.URLError as e:
        """Handle request-related exceptions"""
        print(f"Error occurred: {e}")
