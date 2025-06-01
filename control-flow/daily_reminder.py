#!/usr/bin/env python3
"""
Daily Reminder
This script creates personalized reminders based on task priority and time sensitivity.
"""

def create_reminder():
    # Prompt for task description
    task = input("Enter your task: ")
    
    # Prompt for task priority
    priority = input("Priority (high/medium/low): ").lower()
    
    # Prompt for time sensitivity
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Process task based on priority using match-case
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' is a task with unspecified priority"
    
    # Modify reminder based on time sensitivity
    if time_bound == "yes":
        print(f"Reminder: {reminder} that requires immediate attention today!")
    else:
        print(f"Note: {reminder}. Consider completing it when you have free time.")

create_reminder()