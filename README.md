# Python ToDoList

A command-line task management application built with Python and SQLite.

## About the Project

Python ToDoList is a personal software development project that allows users to manage their tasks through a command-line interface.

The application uses SQLite to store tasks persistently, so they remain available after the program is closed.

This project will evolve over time as I continue to develop, refactor, and improve its functionality.

## Why I Created This Project

I created this project to improve my programming skills and gain practical experience in software development.

Rather than only studying programming concepts, I want to apply them in a real project that I can continuously expand and improve.

By making this project available on GitHub, I can track my progress, document my development process, and build a portfolio that demonstrates my skills as a developer.

## Current Features

* Create tasks
* View saved tasks
* Edit task details
* Change task status
* Update task deadlines
* Add, extend, replace, and remove task notes
* Delete tasks
* Validate date input when creating tasks
* Prevent an end date earlier than the start date when creating tasks
* Store tasks persistently in an SQLite database

## Technologies

* Python
* SQLite
* Git
* GitHub

## Project Structure

```text
Python-ToDoList/
├── main.py
├── database.py
├── README.md
└── .gitignore
```

* **`main.py`** — Handles the command-line menu, user input, and application flow.
* **`database.py`** — Contains functions for retrieving, updating, and deleting tasks and managing task notes.
* **`README.md`** — Documents the project, its features, and how to run it.
* **`.gitignore`** — Specifies files and directories that Git should ignore, such as the local database and Python environment files.

The SQLite database file (`tasks.db`) is created locally when the application runs and should not be committed to Git.

## Getting Started

### Prerequisites

* Python 3
* Git (optional, for cloning the repository)

### Installation

Clone the repository:

```bash
git clone https://github.com/B10rnGustin/Python-ToDoList.git
```

Navigate to the project directory:

```bash
cd Python-ToDoList
```

Run the application:

```bash
python main.py
```

The application creates the SQLite database and the `tasks` table automatically if they do not already exist.

## Future Improvements

Planned improvements may include:

* Task prioritization using the Eisenhower Matrix
* Filtering tasks by status
* Sorting tasks by deadline or priority
* Consistent input validation and error handling
* Automated tests
* Further separation of database operations and application logic
* A graphical user interface (GUI)

## Learning Objectives

Through this project, I aim to improve my understanding of:

* Python programming
* Functions and code organization
* Database operations with SQLite
* Input validation and error handling
* Separation of responsibilities in software applications
* Version control with Git
* Project documentation
* Software development best practices

## Project Status

This project is actively being developed.

The current focus is on improving the code structure by separating database operations from user interaction and making the application more reliable and maintainable.

New features and improvements will be added over time.
