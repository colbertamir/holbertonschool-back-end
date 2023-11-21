#!/usr/bin/python3
"""Gather data from an API and export to CSV"""

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
    todo_url = (
        "https://jsonplaceholder.typicode.com/"
        f"todos?userId={employee_id}"
    )

    try:
        """Fetch user data from API"""
        with urllib.request.urlopen(user_url) as response:
            user_data = json.loads(response.read().decode())

        """Grabs to-do list for the user"""
        with urllib.request.urlopen(todo_url) as response:
            todos = json.loads(response.read().decode())

        """Display user's task completion status & finalized tasks"""
        print(f"Employee {user_data['name']} tasks:")
        for task in todos:
            print(f'"{user_data["id"]}",'
                  f'"{user_data["username"]}",'
                  f'"{str(task["completed"])}",'
                  f'"{task["title"]}"')

    except urllib.error.URLError as e:
        """Handle request-related exceptions"""
        print(f"Error occurred: {e}")
