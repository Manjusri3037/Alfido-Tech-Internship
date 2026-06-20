# Internship Task Tracker
# Python File Handling and Automation Project
# Demonstrates file operations and exception handling

import os
import shutil

try:
    # Create task file
    task_file = "alfido_tasks.txt"

    with open(task_file, "w") as file:
        file.write("Task 1 - Python File Handling - Completed\n")
        file.write("Task 2 - API Integration - Pending\n")
        file.write("Task 3 - Data Analysis - Pending\n")

    print("Task file created successfully.")

    # Read file contents
    print("\nCurrent Internship Tasks:")

    with open(task_file, "r") as file:
        content = file.read()
        print(content)

    # Rename file
    renamed_file = "alfido_progress_report.txt"
    os.rename(task_file, renamed_file)

    print("File renamed successfully.")

    # Move file to folder
    destination_folder = "Completed_Tasks"

    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    shutil.move(
        renamed_file,
        os.path.join(destination_folder, renamed_file)
    )

    print("File moved to Completed_Tasks folder.")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected Error:", e)
