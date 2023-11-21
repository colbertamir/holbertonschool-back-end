#!/usr/bin/python3
"""Gather data from an API and doing CSV"""

from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv

    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{main_url}/users/{argv[1]}/todos"
    user_url = f"{main_url}/users/{argv[1]}"
    
    """Fetching data from JSONplaceholder API"""
    todo_result = get(todo_url).json()
    user_result = get(user_url).json()

    user_id = argv[1]
    user_name = user_result['username']

    """Formatting data for CSV export"""
    todo_list = []
    for todo in todo_result:
        todo_dict = {
            "USER_ID": user_id,
            "USERNAME": user_name,
            "TASK_COMPLETED_STATUS": str(todo.get("completed")),
            "TASK_TITLE": todo.get("title")
        }
        todo_list.append(todo_dict)

    file_name = f"{user_id}.csv"
    """Writing to CSV"""
    with open(file_name, 'w', newline='') as f:
        header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writeheader()
        writer.writerows(todo_list)

    print(f"Task data for employee {user_name} written to {file_name}")

if __name__ == "__main__":
    fetch_and_export_to_csv()
