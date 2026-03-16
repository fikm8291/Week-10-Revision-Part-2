# -------------------------------------------
# Exercise 2: Assessment Revision (Individual Version)
# -------------------------------------------
#
# GOAL:
# 1. Master the "Big Three": Lists, Dictionaries, and While Loops.
# 2. Practice Input Validation: Ensuring data isn't blank or invalid.
# 3. Independent Workflow: Using Git to track your own progress.
# 4. Preparation: Building a complete prototype for Assessment 3.
#
# CONCEPT:
# Real-world programs are "Systems" that run in a loop, collect data 
# into dictionaries, and store those dictionaries in a master list.
#
# INSTRUCTIONS:
# You will write ALL your code at the bottom of this file in the 
# "MAIN PROGRAM CODE" section. As you complete each task, you will 
# expand and refine this single piece of code.
# -------------------------------------------

# -------------------------------------------
# Task 1: System Branding & Data Storage
# -------------------------------------------
# TODO:
# 1. Scroll to the bottom. Ensure the 'tasks' list is initialised.
# 2. Add print statements to create a professional header: "TASK MANAGER".
# 3. Save your file and use Git to Stage and Commit your progress.

# -------------------------------------------
# Task 2: The Logic Loop (Main Menu)
# -------------------------------------------
# TODO:
# 1. Create a variable 'choice' set to "".
# 2. Wrap a 'while' loop around a menu that shows: 
#    1. Add Task, 2. View All, 3. Exit.
# 3. Inside the loop, update 'choice' using input().
# 4. If choice is "3", print "Exiting system..." and let the loop end.
# 5. Save and Commit your progress using Git.

# -------------------------------------------
# Task 3: Capturing & Validating Records
# -------------------------------------------
# TODO:
# 1. Inside your loop, add an 'if choice == "1":' block.
# 2. Ask the user for 'task_name' and 'priority'.
# 3. Validation: Add a nested while loop to ensure 'task_name' isn't blank.
# 4. Create a dictionary for the task and .append() it to your 'tasks' list.
# 5. Save and Commit your progress using Git.

# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: View All Records
# -------------------------------------------
# TODO:
# 1. Add an 'elif choice == "2":' section to your loop.
# 2. If the 'tasks' list is empty, print "No tasks found."
# 3. If it has data, use a 'for' loop to print every task name and priority.
#    HINT: Use f"Task: {task['name']} | Priority: {task['priority']}"

# Extension 2: Menu Gatekeeper (Input Validation)
# -------------------------------------------
# TODO:
# 1. Handle "bad" menu inputs (like typing "9" or "hello").
# 2. Add an 'else:' block at the end of your if/elif chain.
# 3. Print an error message: "Invalid selection, please try again."

# Extension 3: The Search Tool
# -------------------------------------------
# TODO:
# 1. Update your menu to include "4. Search" and change Exit to "5".
# 2. Add an 'elif choice == "4":' section.
# 3. Ask for a search term. Create a 'found' variable set to False.
# 4. Loop through the list. If the name matches, print the task and set found to True.
# 5. After the loop, if found is still False, print "Task not found."

# -------------------------------------------
# ADVANCED ACTIVITY: System Statistics
# -------------------------------------------
# TODO:
# 1. Add a menu option for "Statistics".
# 2. Create a counter variable starting at 0.
# 3. Loop through your list. If a task has a "High" priority, add 1 to the counter.
# 4. Print the total count of all tasks AND the count of High priority tasks.

# ===========================================
#               MAIN PROGRAM CODE
# ===========================================
# Write and update your code here:

tasks = []
