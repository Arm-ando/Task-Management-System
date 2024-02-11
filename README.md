# Task Management System

This project is an extended version of a task management system that uses lists or dictionaries and functions to enhance its functionality. It allows users to register, add tasks, view tasks, and generate reports efficiently.

## Task Overview

The project aims to achieve the following objectives:

1. **Modularity**: The code is structured into functions to improve modularity and readability. Each function serves a specific purpose, such as user registration, task addition, task viewing, and report generation.

2. **User-Friendly Interface**: Users can easily navigate through the system with clear prompts and options. Tasks are displayed in a readable format, and reports provide insightful statistics.

3. **Error Handling**: The system handles errors such as duplicate usernames during registration and ensures that tasks can only be edited if they have not been completed.

4. **Efficiency**: Code efficiency is emphasized to ensure optimal performance. Functions are designed to perform specific tasks effectively, and redundant code is minimized.

## Features

### 1. User Registration (`r`)

- Users can register by providing a unique username and password.
- Duplicate usernames are detected and users are prompted to choose a different username.

### 2. Task Addition (`a`)

- Users can add tasks by specifying details such as the assigned user, task title, description, due date, and completion status.
- Task details are stored in a text file for future reference.

### 3. Task Viewing

#### a. View All Tasks (`va`)

- Users can view all tasks stored in the system.
- Tasks are displayed in a user-friendly format, making it easy to understand their details.

#### b. View My Tasks (`vm`)

- Users can view tasks assigned to them.
- Tasks are displayed with options to mark them as complete or edit their details if they are not yet completed.

### 4. Reports Generation (`gr`)

- Admin users can generate reports on task statistics.
- Reports include information such as the total number of tasks, completed tasks, incomplete tasks, overdue tasks, and percentages of completion and overdue tasks.

### 5. Display Statistics (`d`)

- Users can view statistics such as the total number of tasks, total number of users, tasks assigned to them, and percentages of completion, incompleteness, and overdue tasks assigned to them.

