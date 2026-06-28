## Court Case Management System

### Overview

This project was developed as part of a Data Structures and Algorithms assignment. The objective was to design and implement a court case management system that demonstrates the practical use of multiple data structures and algorithms within a single application.

The system supports adding, storing, searching, sorting, and displaying court cases while showcasing how different data structures solve different computational problems efficiently.

------

## Features

- Add new court cases
- View cases in order of arrival
- View cases ordered by priority
- Search for a case using its Case ID
- Sort cases by priority
- Demonstrate the performance difference between hash-based and linear search

------

## Data Structures and Algorithms

### Linked List

The linked list stores court cases in the order they are received.

This allows the system to preserve the chronological order of incoming cases and efficiently append new cases to the end of the list.

------

### Binary Search Tree (BST)

Each court case contains:

```text
Case Name
Case ID
Priority
```

The Binary Search Tree organizes cases according to their priority.

This gives efficient traversal of cases from highest priority to lowest priority without having to sort the data every time.

------

### Hash Table

The hash table provides fast lookup of court cases using their unique Case ID.

The custom hash function:

1. Converts each character in the Case ID into its Unicode value.
2. Sums those values.
3. Computes the index using the modulo operator.

When two Case IDs map to the same index, collisions are handled using **separate chaining**, where each bucket stores a list of cases.

------

### Insertion Sort

Insertion Sort is used to produce a sorted list of court cases based on their priority.

The algorithm collects all cases stored in the hash table before sorting them in ascending order of priority.

Although more advanced sorting algorithms exist, Insertion Sort was selected to demonstrate a fundamental sorting algorithm as required by the assignment.

------

## Technologies Used

- Python
- Linked Lists
- Binary Search Trees
- Hash Tables
- Insertion Sort
- Object-Oriented Programming

------

## What I Learned

This project strengthened my understanding of:

- Designing systems using multiple data structures.
- Selecting the appropriate data structure for a specific task.
- Implementing custom hash functions.
- Collision handling using separate chaining.
- Binary Search Tree traversal.
- Applying sorting algorithms to real-world data.
- Object-oriented programming in Python.

------

## Future Improvements

- Balance the Binary Search Tree (AVL or Red-Black Tree).
- Replace Insertion Sort with Merge Sort or Quick Sort for larger datasets.
- Store court cases in a database instead of memory.
- Develop a graphical user interface.
- Add persistent storage and user authentication.